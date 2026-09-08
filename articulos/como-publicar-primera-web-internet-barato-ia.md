---
layout: article
title: "Cómo publicar tu primera web en internet por menos de 5€ con IA"
description: "Te cuento cómo publiqué mi primera web en internet barato con IA gastando menos de 5€, paso a paso y con errores incluidos."
category: "Guía"
date: 2026-09-06
readtime: 8
affiliate_text: "Si quieres alojar tu proyecto sin complicarte, yo usé Hostinger y me fue bien"
affiliate_url: "https://www.hostinger.com"
affiliate_label: "Probar Hostinger"
---

Hace un mes tenía un proyecto de clase (una web para gestionar tareas de un grupo de estudio) metido en local, corriendo solo en mi ordenador, y me di cuenta de que llevaba semanas diciendo "esto lo subo pronto" sin subirlo nunca. El miedo no era el código, era todo lo de alrededor: dominio, hosting, certificados, DNS... cosas que en DAW nos explican por encima y que en la práctica dan bastante pereza. Así que me puse un objetivo tonto pero motivador: publicar mi primera web en internet barato con IA, gastando lo menos posible, y usando ChatGPT y Claude como apoyo cada vez que me atascara. Spoiler: al final me gasté 4,80€ y tardé una tarde de sábado, no un mes.

## Por qué quería que fuera barato (y por qué no hace falta gastar más)

Cuando buscas "cómo subir mi web" te salen mil tutoriales que asumen que tienes presupuesto de startup. Planes de hosting a 15€/mes, dominios .com a precio completo, certificados SSL de pago... y yo soy estudiante, no tengo ese dinero para un proyecto que ni siquiera sé si va a tener usuarios reales. La buena noticia es que en 2026 esto ya no es necesario. Los hostings tipo Hostinger tienen planes compartidos que bajan a poco más de 2€ al mes si contratas por varios meses de golpe, y los certificados SSL vienen gratis prácticamente en todos los sitios. La parte que sí cuesta dinero de verdad es el dominio, y ahí es donde entra la segunda pieza del combo.

Yo comparé precios en Namecheap antes de decidirme, porque tienen promociones agresivas en dominios menos habituales (.xyz, .site, .online) que te dejan el primer año por menos de 2€, frente a los 10-12€ que pide un .com normal. Si tu proyecto es una prueba, un portfolio o algo para clase, no pasa nada por no llevar un .com: nadie te va a juzgar por tener un dominio .site cuando lo que importa es lo que hay dentro.

### Cómo repartí el presupuesto real

Al final mis 4,80€ se fueron así: 1,80€ por un dominio .site en Namecheap con descuento de primer año, y 2,99€ del primer mes de hosting compartido en Hostinger, que además incluía SSL gratuito y un asistente de instalación con un paso a paso bastante claro para quien no ha tocado un panel de hosting en su vida. No metí publicidad de por medio, ni upsells de "protección de dominio" que te intentan colar en el checkout: eso lo desmarqué todo.

## Dónde entra la IA en publicar tu primera web

Aquí es donde la cosa se pone interesante para alguien que estudia DAW, porque la IA no publicó la web por mí, pero me ahorró las horas muertas de buscar en foros. Le pedí a Claude que me explicara qué era exactamente un registro DNS tipo A y por qué mi dominio no apuntaba al hosting después de dos horas de espera (resulta que solo tenía que tener paciencia, la propagación DNS tarda). También usé IA para revisar mi archivo `.htaccess` cuando mi web en Flask no cargaba bien las rutas en el servidor compartido, algo que en local nunca me había dado problemas porque ahí no hay reescritura de URLs configurada igual.

Lo que no hice fue pedirle a la IA que me generara el código de la web entero sin entenderlo, porque entonces cuando algo se rompe en producción (y algo se rompe siempre) no tienes ni idea de por dónde tirar. La usé como un compañero que sabe de servidores, no como el que hace el trabajo.

## Paso a paso de cómo subí mi web sin gastar de más

Primero compré el dominio en Namecheap, sin activar ningún complemento adicional; solo el dominio pelado. Después contraté el hosting compartido más básico de Hostinger, el que viene con un solo sitio web permitido, que es todo lo que necesitaba para este proyecto. Luego conecté el dominio al hosting cambiando los nameservers desde el panel de Namecheap hacia los que me dio Hostinger, ese paso fue el único que me dio verdadero dolor de cabeza porque tardó casi 6 horas en propagarse y yo creía que lo había roto todo.

Con el dominio ya apuntando bien, subí mi proyecto por FTP usando FileZilla, que es gratuito, y activé el SSL desde el propio panel de Hostinger con un clic, sin necesidad de tocar terminal ni configurar nada de Let's Encrypt a mano. Y ya. En menos de un día tenía mi tarea de clase corriendo en un dominio real, con https y todo.

## Lo que aprendí y lo que cambiaría

Si tuviera que repetirlo, contrataría el hosting por 12 meses en vez de por 1, porque el precio mensual baja bastante y al final pagas menos en total aunque desembolses más de golpe. También esperaría a tener el proyecto un poco más pulido antes de publicarlo, porque en cuanto subí la web me dio vergüenza que un profesor la viera con el diseño a medias que tenía. Pero de eso va esto: aprender publicando de verdad, no simulando en local para siempre.

Si estás en la misma situación que yo hace un mes, con un proyecto guardado esperando a que le tengas menos miedo al despliegue, te diría que el bloqueo suele ser mental, no técnico ni económico. Por menos de 5€ puedes tener tu propia web real en internet este mismo fin de semana.
