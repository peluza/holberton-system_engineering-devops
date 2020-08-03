Background Context


When I was working for SlideShare, I worked on an auto-remediation tool called Skynet that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent nil to the filter method.

There were 2 pieces of bad news:

When MCollective receives nil as an argument for its filter method, it takes this to mean ‘all servers’
The action I sent was to terminate the selected servers
I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos… Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.



That was me ^_^‘: https://twitter.com/devopsreact/status/836971570136375296

Resources
Read or watch:

Intro to Configuration Management
Puppet resource type: file (check “Resource types” for all manifest types in the left menu)
Puppet’s Declarative Language: Modeling Instead of Scripting
Puppet lint
Puppet emacs mode
Requirements
General
All your files will be interpreted on Ubuntu 14.04 LTS
All your files should end with a new line
A README.md file at the root of the folder of the project is mandatory
Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
Sus manifiestos de Puppet deben ejecutarse sin error
La primera línea de su manifiesto de Puppet debe ser un comentario que explique de qué se trata el manifiesto de Puppet
Los archivos de manifiesto de Puppet deben terminar con la extensión .pp
Nota sobre versiones
Su VM Ubuntu 14.04 debería tener Puppet 3.4 preinstalado.

No es necesario que intente actualizar las versiones. Este proyecto es simplemente un conjunto de tareas para familiarizarlo con la sintaxis de nivel básico que es prácticamente idéntica en las versiones más recientes de Puppet.

La documentación vinculada es a Puppet 3.8 porque la documentación 3.4 se ha archivado y, por lo tanto, es más difícil de navegar. Si de todos modos desea actualizar, haga clic aquí (esto no afectará la forma en que se verifica su código). Puppet 5 Docs

Instalar en pc puppet-lint
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
