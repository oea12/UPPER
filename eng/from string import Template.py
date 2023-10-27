from string import Template

# Tu plantilla HTML
template_str = '''
<div class="grid-item running trainer" data-pg-collapsed> 
    <div class="trainer-item"> 
        <div class="trainer-thumb" data-pg-collapsed> 
            <img src="assets/images/trainer/trainer-1.png" alt="trainer"> 
            <div class="trainer-overlay" data-pg-collapsed> 
                <div class="share-area"> 
                    <div class="share-icon"> <i class="fas fa-share-alt"></i> 
                    </div>                     
                    <ul class="social-list"> 
                        <li>
                            <a href="${facebook_link}"><i class="fab fa-facebook-f"></i></a>
                        </li>                         
                        <li>
                            <a href="${instagram_link}"><i class="fab fa-instagram"></i></a>
                        </li>                         
                    </ul>                     
                </div>                 
            </div>             
        </div>         
        <div class="trainer-content" data-pg-collapsed> 
            <h3 class="title"><a onclick="loadFighter(1)" href="${tapology_link}">${name}</a></h3> <span class="sub-title">${weight_class}</span> 
        </div>         
    </div>     
</div>
'''

# Crear un objeto de plantilla
template = Template(template_str)

# Tus datos
data = [
    {'name': 'Andrea Vazquez', 'weight_class': 'Strawweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/281167-andrea-vazquez', 'instagram_link': 'https://www.instagram.com/andreavrmma/', 'facebook_link': 'https://www.facebook.com/AndreaVazquez'},
    {'name': 'Nicole Geraldo', 'weight_class': 'Strawweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/225054-nicole-geraldo', 'instagram_link': 'https://www.instagram.com/nicogeraldocruz/', 'facebook_link': 'https://www.facebook.com/NicoGeraldo'},
    {'name': 'Yazmin Najera', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/272406-yazmin-najera', 'instagram_link': 'https://www.instagram.com/yazminajera/', 'facebook_link': None},
    {'name': 'Abril Viridiana', 'weight_class': 'Strawweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/311796-abril-aranda', 'instagram_link': None, 'facebook_link': None},
    {'name': 'Victoria Alba', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/302866-victoria-alba', 'instagram_link': 'https://www.instagram.com/victoria_albba/', 'facebook_link': None},
    {'name': 'Alba Almanza', 'weight_class': 'Strawweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/356593-alva-almanza', 'instagram_link': None, 'facebook_link': None},
    {'name': 'Alex Garzon', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/342124-alex-garzon-gutierrez', 'instagram_link': 'https://www.instagram.com/alexgarzon503/', 'facebook_link': None},
    {'name': 'Alexis Coatzin', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/342123-alexis-coatzin-santillan', 'instagram_link': 'https://www.instagram.com/alexiscoatzin/', 'facebook_link': None},
    {'name': 'Bryan Arreaga', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/107983-bryan-arreaga', 'instagram_link': 'https://www.instagram.com/bryanarreaga/', 'facebook_link': None},
    {'name': 'Carlos Camargo', 'weight_class': 'Lightweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/295203-carlos-camargo-drago', 'instagram_link': 'https://www.instagram.com/drago_camargomma/', 'facebook_link': None},
    {'name': 'Carlos Rivera', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/89832-carlos-rivera-lobo', 'instagram_link': 'https://www.instagram.com/carloslobo93/', 'facebook_link': None, 'twitter_link': None},
    {'name': 'Daniel Zellhuber', 'weight_class': 'Lightweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/156784-daniel-olvera-zellhuber-zellhuber', 'instagram_link': 'https://www.instagram.com/daniel_zellhuber/', 'facebook_link': 'https://www.facebook.com/DanielGoldenBoyZellhuber', 'twitter_link': 'https://twitter.com/GoldenboyZell'},
    {'name': 'David Mendoza', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/117354-david-mendoza', 'instagram_link': 'https://www.instagram.com/davidmendoza.mma/', 'facebook_link': 'https://www.facebook.com/DavidLeonMendoza', 'twitter_link': None},
    {'name': 'Hugo Flores', 'weight_class': 'Lightweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/131817-hugo-flores-hooligan', 'instagram_link': 'https://www.instagram.com/hooligan.mma/', 'facebook_link': 'https://www.facebook.com/HugoHooliganFlores', 'twitter_link': None},
    {'name': 'Irvin Amaya', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/79104-irvin-amaya', 'instagram_link': 'https://www.instagram.com/irvinthestorm/', 'facebook_link': 'https://www.facebook.com/IrvinTheStormAmaya', 'twitter_link': 'https://twitter.com/irvinthestorm'},
    {'name': 'Ivan Valenzuela', 'weight_class': 'Middleweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/198169-ivan-valenzuela', 'instagram_link': 'https://www.instagram.com/ivanbambam92/', 'facebook_link': 'https://www.facebook.com/IvanValenzuelaMolinaBamBam', 'twitter_link': None},
    {'name': 'Sergio Cossio', 'weight_class': 'Lightweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/89392-daniel-cossio', 'instagram_link': 'https://www.instagram.com/drakossio/', 'facebook_link': 'https://www.facebook.com/SergioCossio', 'twitter_link': None},
    {'name': 'Fernando Saavedra', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/187435-fernando-saavedra-virus', 'instagram_link': 'https://www.instagram.com/virus_saavedra/', 'facebook_link': 'https://www.facebook.com/FernandovirusSaavedra', 'twitter_link': None},
    {'name': 'Luis Ronaldo Rodriguez', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/165024-luis-rodrguez-lazyboy', 'instagram_link': 'https://www.instagram.com/lazyboy.mma/', 'facebook_link': 'https://www.facebook.com/LuisRonaldoLazyboyRodriguez', 'twitter_link': None},
    {'name': 'Yair Rodriguez', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/70995-yair-rodriguez', 'instagram_link': 'https://www.instagram.com/panteraufc/', 'facebook_link': 'https://www.facebook.com/YairRodriguezElPantera', 'twitter_link': None},
    {'name': 'Yoav Alejandro', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/338102-yoav-bobadilla-el-gallo', 'instagram_link': 'https://www.instagram.com/yoav.bobadilla/', 'facebook_link': None, 'twitter_link': None},
    {'name': 'Guillermo Vidañez', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/146263-guillermo-antonio-vidanez-zapien', 'instagram_link': 'https://www.instagram.com/guillermozapien23/', 'facebook_link': None, 'twitter_link': None},
    {'name': 'Rafael Espino', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/236510-rafael-espino', 'instagram_link': None, 'facebook_link': None, 'twitter_link': None},
    {'name': 'Salvador Osorio', 'weight_class': 'Middleweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/356591-salvador-osorio', 'instagram_link': 'https://www.instagram.com/salvador.osoriog/', 'facebook_link': None, 'twitter_link': None},
    {'name': 'Ramon Cardozo', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/122553-ramon-cardoso', 'instagram_link': 'https://www.instagram.com/ramoncardozo94/', 'facebook_link': 'https://www.facebook.com/RamonCCardozo', 'twitter_link': None},
    {'name': 'Rafael Saenz', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/231947-rafael-saenz', 'instagram_link': 'https://www.instagram.com/saenz.polo34/', 'facebook_link': None, 'twitter_link': None},
    {'name': 'Pedro Rubio', 'weight_class': 'Lightweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/311806-pedro-rubio', 'instagram_link': 'https://www.instagram.com/rubiosambranopeter/', 'facebook_link': None, 'twitter_link': None},
    {'name': 'Jesus Siller', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/189671-jesus-siller', 'instagram_link': 'https://www.instagram.com/shurro_sin_mota/', 'facebook_link': None, 'twitter_link': None},
    {'name': 'Paulino Siller', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/96125-paulino-siller', 'instagram_link': 'https://www.instagram.com/paulino_sille', 'facebook_link': 'https://www.facebook.com/CuateSillerPeleadorMMA'},
    {'name': 'Pablo Tirado', 'weight_class': 'Lightweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/311802-pablo-tirado', 'instagram_link': 'https://www.instagram.com/pablotirado', 'facebook_link': None},
    {'name': 'Luis Guerrero', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/107701-luis-guerrero-pantera', 'instagram_link': 'https://www.instagram.com/pantera.guerrero', 'facebook_link': 'https://www.facebook.com/PanteraGuerrero'},
    {'name': 'Jorge Alberto Garcia', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/237338-jorge-garcia-beto', 'instagram_link': 'https://www.instagram.com/_beto__panda', 'facebook_link': None},
    {'name': 'Irving Cardona', 'weight_class': 'Lightweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/244996-irving-macias-mustang', 'instagram_link': 'https://www.instagram.com/irving_cardona_macias', 'facebook_link': None},
    {'name': 'Hector Ferral', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/99402-hector-diaz', 'instagram_link': 'https://www.instagram.com/hecferral', 'facebook_link': 'https://www.facebook.com/HectorFerralPerez'},
    {'name': 'Emmanuel Blancas', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/333467-emmanuel-blancas', 'instagram_link': 'https://www.instagram.com/blaancass', 'facebook_link': None},
    {'name': 'Diego Rosales', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/275867-diego-rosales', 'instagram_link': 'https://www.instagram.com/ninja_rosales', 'facebook_link': None},
    {'name': 'Alejandro Villareal', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/288039-alejandro-villarreal-titi', 'instagram_link': 'https://www.instagram.com/alex_villarreal67', 'facebook_link': None},
    {'name': 'Anuar Aburto', 'weight_class': 'Welterweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/306445-anuar-aburto', 'instagram_link': 'https://www.instagram.com/anuaraburto', 'facebook_link': 'https://www.facebook.com/TarzanAburto'},
    {'name': 'Brandon Santillan', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/318201-brandon-santillan', 'instagram_link': 'https://www.instagram.com/s.a.n.t.i.l.l.a.n', 'facebook_link': None},
    {'name': 'Arturo Uziel', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/311171-arturo-lopez', 'instagram_link': 'https://www.instagram.com/uziel.gmz', 'facebook_link': None},
    {'name': 'Angel Altamirano', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/338103-angel-altamirano-kain', 'instagram_link': 'https://www.instagram.com/kainaltamirano', 'facebook_link': None},
    {'name': 'Alejandro Medellin', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.sherdog.com/fighter/Alex-Medellin-390336', 'instagram_link': 'https://www.instagram.com/alexmedemma', 'facebook_link': None},
    {'name': 'Juan José Zuñiga', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/356588-juan-zungia', 'instagram_link': 'https://www.instagram.com/juan_el_alima.a_', 'facebook_link': None},
    {'name': 'Mauricio Partida', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/194730-mauricio-partida', 'instagram_link': 'https://www.instagram.com/mauricioalfonso_mma', 'facebook_link': None},
    {'name': 'Luis Daniel Reyes Ortega', 'weight_class': 'Lightweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/398366-daniel-reyes', 'instagram_link': 'https://www.instagram.com/danielreyes_145', 'facebook_link': None},
    {'name': 'Axel Osuna', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/199416-axel-osuna', 'instagram_link': 'https://www.instagram.com/axelosuna.mma', 'facebook_link': None},
    {'name': 'Cesar Vazquez', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/249311-cesar-vazquez-demoledor-jr', 'instagram_link': 'https://www.instagram.com/soydemoledorjr_mma', 'facebook_link': None},
    {'name': 'Luis Ivan Rodriguez', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/306446-luis-ivan-rodriguez', 'instagram_link': 'https://www.instagram.com/luisivan.rodriguez125/', 'facebook_link': None},
    {'name': 'Charlie Decca', 'weight_class': 'Lightweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/115296-charles-decca', 'instagram_link': 'https://www.instagram.com/charlie_decca/', 'facebook_link': None},
    {'name': 'Elvin Espinoza', 'weight_class': 'Lightweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/115298-elvin-espinoza', 'instagram_link': 'https://www.instagram.com/elvinespinoza_/', 'facebook_link': None},
    {'name': 'Brahyan Zurcher', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/98826-bryhayn-zurcher', 'instagram_link': 'https://www.instagram.com/brahyanzurcher/', 'facebook_link': None},
    {'name': 'Rosselyn Chavira', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/164886-rosselyn-chavira', 'instagram_link': 'https://www.instagram.com/chulamma/', 'facebook_link': None},
    {'name': 'Martin Davila', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/78560-martin-davila', 'instagram_link': 'https://www.instagram.com/martydmmabjj/', 'facebook_link': None},
    {'name': 'Victor Flor', 'weight_class': 'Flyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/84644-victor-flor', 'instagram_link': 'https://www.instagram.com/mmavic954/', 'facebook_link': None},
    {'name': 'Chris Quiroz', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/235731-chris-quiroz', 'instagram_link': 'https://www.instagram.com/chapoquirozz/', 'facebook_link': None},
    {'name': 'Hunter Starner', 'weight_class': 'Bantamweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/240181-hunter-starner', 'instagram_link': 'https://www.instagram.com/showtimestarner/', 'facebook_link': None},
    {'name': 'Josh Blyden', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/45497-josh-blyden', 'instagram_link': 'https://www.instagram.com/joshblydenmma/', 'facebook_link': None},
    {'name': 'Justin Vazquez', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/150228-justin-vasquez', 'instagram_link': 'https://www.instagram.com/slickj145/', 'facebook_link': None},
    {'name': 'Martin Justiz', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/168478-martin-justiz', 'instagram_link': 'https://www.instagram.com/martinjustiz_/', 'facebook_link': None},
    {'name': 'Brandon Moran', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/143921-brandon-moran', 'instagram_link': 'https://www.instagram.com/bmoran_mma/', 'facebook_link': None},
    {'name': 'Cedric Gunninson', 'weight_class': 'Lightweight', 'tapology_link': None, 'instagram_link': 'https://www.instagram.com/gunmangunninson/', 'facebook_link': None},
    {'name': 'Marcos Lloreda', 'weight_class': 'Welterweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/59555-marcos-lloreda', 'instagram_link': 'https://www.instagram.com/m_yoreda316/', 'facebook_link': None},
    {'name': 'Carlos Martinez', 'weight_class': 'Middleweight / Light heavyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/218580-carlos-martinez', 'instagram_link': 'https://www.instagram.com/losmar97/', 'facebook_link': None},
    {'name': 'Everett Sims', 'weight_class': 'Heavyweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/20914-everitt-sims', 'instagram_link': 'https://www.instagram.com/simschocolate/', 'facebook_link': None},
    {'name': 'Silvestre Sánchez Montes', 'weight_class': 'Lightweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/194194-cesar-garcia', 'instagram_link': 'https://www.instagram.com/sanchezmontess/', 'facebook_link': None},
    {'name': 'Levy Marroquin', 'weight_class': 'Lightweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/63983-saul-marroquin-el-negro', 'instagram_link': 'https://www.instagram.com/levy_marroquin/', 'facebook_link': None},
    {'name': 'Jaír Perez', 'weight_class': 'Featherweight', 'tapology_link': 'https://www.tapology.com/fightcenter/fighters/135229-jair-prez', 'instagram_link': 'https://www.instagram.com/jairperezmma/', 'facebook_link': None},

]

# Abre un archivo en modo escritura
with open('output.txt', 'w') as f:
    # Generar HTML para cada conjunto de datos
    for d in data:
        try:
            rendered_html = template.substitute(d)
            f.write(rendered_html + '\n')
        except KeyError as e:
            print(f"Falta la clave {e} en el diccionario")