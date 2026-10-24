export default async function handler(req, res) {
  // CORS headers para permitir peticiones desde el blog
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Responder a preflight OPTIONS
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // Permitir solo POST
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Usa el método POST' });
  }

  const { codigo, error, lenguaje } = req.body;

  if (!codigo) {
    return res.status(400).json({ error: 'Falta el código' });
  }

  const GROQ_API_KEY = process.env.GROQ_API_KEY;

  if (!GROQ_API_KEY) {
    return res.status(500).json({ error: 'Falta configurar la API key en el servidor' });
  }

  const prompt = `Eres un profesor de programación paciente y claro, especializado en ayudar a estudiantes principiantes.

El usuario te envía este código (${lenguaje || 'Java'}):

\`\`\`
${codigo}
\`\`\`

Y este error de consola (si lo hay):
${error || 'No hay error de consola, solo quiere revisar que el código esté bien'}

Tu trabajo es devolver, EN CASTELLANO y de forma muy sencilla:

1. Explicación del problema en pasos simples (máximo 4 pasos, lenguaje claro, sin tecnicismos innecesarios).
2. El código corregido completo y listo para copiar y pegar.
3. Una pregunta tipo test con 3 opciones (A, B, C) para verificar que el usuario entiende POR QUÉ fallaba el código.
4. La respuesta correcta (letra A, B o C).

Responde ÚNICAMENTE con un objeto JSON válido, sin texto antes ni después, con esta estructura exacta:
{
  "explicacion": "Explicación sencilla en castellano",
  "codigoCorregido": "Código completo corregido",
  "preguntaTest": "Pregunta de comprensión?",
  "opciones": ["A) Primera opción", "B) Segunda opción", "C) Tercera opción"],
  "respuestaCorrecta": "A"
}

No uses markdown, no pongas \`\`\`json, devolve solo el JSON puro.`;

  try {
    const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${GROQ_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'llama-3.1-8b-instant',
        messages: [{ role: 'user', content: prompt }],
        temperature: 0.3,
        max_tokens: 1500
      })
    });

    const data = await response.json();
    const content = data.choices[0].message.content;

    let resultado;
    try {
      resultado = JSON.parse(content);
    } catch (e) {
      resultado = {
        explicacion: content,
        codigoCorregido: '',
        preguntaTest: '',
        opciones: [],
        respuestaCorrecta: ''
      };
    }

    return res.status(200).json(resultado);
  } catch (err) {
    let errMsg = 'Error desconocido';
    if (err) {
      errMsg = err.message || err.toString() || 'Error desconocido';
    }
    return res.status(500).json({
      explicacion: 'Error del servidor: ' + errMsg,
      codigoCorregido: '',
      preguntaTest: '',
      opciones: [],
      respuestaCorrecta: ''
    });
  }
}