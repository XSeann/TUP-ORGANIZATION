HEAD =  '''
        <div class="header"></div>
        <div class="justin">
            <div class="logo">
                <img src="static/tup logo.png" alt="TUP Logo">
                <div class="logo-text">
                    <div class="university-name">TECHNOLOGICAL UNIVERSITY OF THE PHILIPPINES</div>
                    <div class="tagline">SERVING WITH PURE PASSION AND DEDICATION</div>
                </div>
            </div>
            <div class="time" id="time-container">
                <div>PHILIPPINES STANDARD TIME</div>
                <div id="current-time"></div>
            </div>
       </div>

        <nav>
            <form action="/home" id="homeForm">
                <input type="submit" value="Home"/>
            </form>
            <a href="">UPCOMING EVENTS</a>
            <a href="Front Page.html#abt">ABOUT</a>
            <a href="Front Page.html#nonc">ORGANIZATIONS</a>
            <form action="/logout" id="logoutForm">
                <input type="submit" value="Log Out"/>
            </form>
        </nav>

        <script>
            function updateTime() {
                const timeContainer = document.getElementById('current-time');
                const now = new Date();

                const options = {
                    weekday: 'long',
                    month: 'long',
                    day: 'numeric',
                    hour: '2-digit',
                    minute: '2-digit',
                    second: '2-digit',
                    hour12: true,
                    timeZone: 'Asia/Manila'
                };

                timeContainer.textContent = now.toLocaleString('en-US', options);
            }

            setInterval(updateTime, 1000);

            updateTime();
        </script>
        '''

BOLTUP = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>Boluntaryong TUPians</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/BOLTUPGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/BOLTUPRES.jpg" alt="pres-pic">
                <div>
                    <strong>Jennifer Asne Malong</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>BOLTUP's Vision</h2>
                    <p>We envision a community where fellow and aspiring TUPians, 
                        driven by a genuine love for the university, find a supportive 
                        space to enhance their skills, abilities, and leadership 
                        potential. Our goal is to contribute to the development of a well-
                        organized, career-oriented university community. The volunteers 
                        of Boluntaryong TUPians are steadfast in their passion and 
                        dedication to empowering and assisting students in realizing 
                        this vision.
                    </p>

                    <h2>BOLTUP's Mission</h2>
                    <p>(a) To respond to students’ inquiries in a manner that is consistent, 
                        appropriate, and authentic, ensuring that all interactions uphold the 
                        organization’s standards and values.
                        (b) To provide a platform where students can directly express their 
                        concerns and suggestions. This platform will facilitate open inquiry 
                        and dialogue, encouraging continuous development and necessary 
                        modifications within the system.
                        (c) To offer students opportunities to explore and enhance their skills 
                        and abilities through a variety of collaborative programs and activities 
                        designed to foster personal and academic growth.
                    </p>
                </div>
            </div>
            
            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>TUP Foundation Week</h1>
                <p>December 18 - 21, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/BOLTUP/BOLTUP2.JPG" alt="bol1">
                        <img src="static/Projects/BOLTUP/BOLTUP2.2.JPG" alt="bol2">
                        <img src="static/Projects/BOLTUP/BOLTUP2.3.JPG" alt="bol3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>

            <div class="container">
                <h1>Outreach Program</h1>
                <p>December 7, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/BOLTUP/BOLTUP3.JPG" alt="bol1">
                        <img src="static/Projects/BOLTUP/BOLTUP3.2.JPG" alt="bol2">
                        <img src="static/Projects/BOLTUP/BOLTUP3.3.JPG" alt="bol3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>

            <div class="container">
                <h1>Manila Bay Coastal Clean Up Drive</h1>
                <p>September 28, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/BOLTUP/BOLTUP1.JPG" alt="bol1">
                        <img src="static/Projects/BOLTUP/BOLTUP1.2.JPG" alt="bol2">
                        <img src="static/Projects/BOLTUP/BOLTUP1.3.JPG" alt="bol3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="BOLTUP">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
        '''

CYC = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>College Y Club</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/CYCGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/Missing.png" alt="pres-pic">
                <div>
                    <strong>Daniel Alexandrei R. Esperida</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>College Y Club's Vision</h2>
                    <p>Aliquam sed elit ex. Quisque sit amet fermentum diam. In posuere, mauris vel mattis efficitur, eros ipsum malesuada purus, id ornare velit arcu id nunc. Nunc quis dapibus nisl, a tempus lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer mi purus, ornare quis efficitur id, tempor eu arcu. Ut dapibus rhoncus nisl, et finibus mauris.</p>
                    <h2>College Y Club's Mission</h2>
                    <p>Maecenas finibus, nisl vitae interdum laoreet, lorem tortor hendrerit leo, vel pellentesque tellus ligula quis magna. Donec tristique purus massa, ac faucibus enim ultrices vel. Mauris quam urna, sodales non fermentum nec, pharetra tempor ligula. Vestibulum tempor tellus quis vehicula tristique. Etiam augue arcu, eleifend ac augue vitae, tristique sollicitudin orci.</p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>TUP Foundation Week</h1>
                <p>December 18 - 21, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/CYC/CYC1.2.jpg" alt="cyc 1">
                        <img src="static/Projects/CYC/CYC1.2.jpg" alt="cyc 2">
                        <img src="static/Projects/CYC/CYC1.3.jpg" alt="cyc 3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>
            
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="CYC">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
GDG = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>Google Developer Groups on Campus TUP Manila</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/GDGCGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/GDGPRES.jpg" alt="pres-pic">
                <div>
                    <strong>Jhondel Mico N. Abas</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>GDGC's Vision</h2>
                    <p>This organization envisions itself as a community of developers that are
                        passionate about uplifting communities through technology and
                        innovation.</p>
                    <h2>GDGC's Mission</h2>
                    <p>This organization has the mission to:<br>
                        (1) Empower people through technology and programming education<br>
                        (2) Enlighten them to the power of innovation and problem-solving<br>
                        (3) Nurture them to create meaningful technological solutions for the
                        community.</p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>TUP Foundation Week</h1>
                <p>December 18 - 21, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/GDGC/GDGC1.jpg" alt="D 1">
                        <img src="static/Projects/GDGC/GDGC2.jpg" alt="D 2">
                        <img src="static/Projects/GDGC/GDGC3.jpg" alt="D 3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="GDG">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
KPL = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>Kabataan Partylist - TUP</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/KPLGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/Missing.png" alt="pres-pic">
                <div>
                    <strong>Jeanline O. Bangcal</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>KPL-TUP's Vision</h2>
                    <p>
                        Aliquam sed elit ex. Quisque sit amet fermentum diam. In posuere, mauris vel mattis efficitur, 
                        eros ipsum malesuada purus, id ornare velit arcu id nunc. Nunc quis dapibus nisl, a tempus 
                        lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer mi purus, ornare quis 
                        efficitur id, tempor eu arcu. Ut dapibus rhoncus nisl, et finibus mauris.
                    </p>

                    <h2>KPL-TUP's Mission</h2>
                    <p>
                        Maecenas finibus, nisl vitae interdum laoreet, lorem tortor hendrerit leo, vel pellentesque 
                        tellus ligula quis magna. Donec tristique purus massa, ac faucibus enim ultrices vel. Mauris 
                        quam urna, sodales non fermentum nec, pharetra tempor ligula. Vestibulum tempor tellus quis 
                        vehicula tristique. Etiam augue arcu, eleifend ac augue vitae, tristique sollicitudin orci. 
                        Donec auctor tincidunt arcu vel aliquet. Curabitur est mi, pulvinar eu porta ac, consequat at 
                        libero. Etiam sit amet magna sed mi ornare congue a a arcu.
                    </p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>Student Congress</h1>
                <p>December 3 - 5, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/KPL/KPL1.jpg" alt="bol1">
                        <img src="static/Projects/KPL/KPL2.jpg" alt="bol2">
                        <img src="static/Projects/KPL/KPL3.jpg" alt="bol3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="KPL">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
OSESH = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>Organization of Students for Environmental Safety and Health</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/OSESHGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/Missing.png" alt="pres-pic">
                <div>
                    <strong>Christian Lorrenze T. Filomeno</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>OSESH's Vision</h2>
                    <p>Maecenas finibus, nisl vitae interdum laoreet, lorem tortor hendrerit leo, vel pellentesque tellus ligula quis magna. Donec tristique purus massa, ac faucibus enim ultrices vel. Mauris quam urna, sodales non fermentum nec, pharetra tempor ligula. Vestibulum tempor tellus quis vehicula tristique. Etiam augue arcu, eleifend ac augue vitae, tristique sollicitudin orci. Donec auctor tincidunt arcu vel aliquet. Curabitur est mi, pulvinar eu porta ac, consequat at libero. Etiam sit amet magna sed mi ornare congue a a arcu.</p>
                    <h2>OSESH's Mission</h2>
                    <p>Aliquam sed elit ex. Quisque sit amet fermentum diam. In posuere, mauris vel mattis efficitur, eros ipsum malesuada purus, id ornare velit arcu id nunc. Nunc quis dapibus nisl, a tempus lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer mi purus, ornare quis efficitur id, tempor eu arcu. Ut dapibus rhoncus nisl, et finibus mauris.</p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>CleanTramuros Clean Up Drive</h1>
                <p>April 21, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/OSESH/osesh1.jpg" alt="bol1">
                        <img src="static/Projects/OSESH/osesh2.jpg" alt="bol2">
                        <img src="static/Projects/OSESH/osesh3.jpg" alt="bol3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="OSESH">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
SMERS = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>Students' Multimedia Even Reporters Society</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/SMERSGP.jfif" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/SMERSPRES.jpg" alt="pres-pic">
                <div>
                    <strong>Teofista Kyla J. Dineros</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>SMERS's Vision</h2>
                    <p>The TUP Students’ Multimedia Event Reporters Society (SMERS) develops the students interest to interact, practice communication skills, and enhance the ability for creating multimedia. It shall endeavor to develop citizen workers who will be careful, innovative, competent, knowledgeable, morally upright, and responsible media men to the university faculty and students.</p>
                    <h2>SMERS's Mission</h2>
                    <p>The TUP Students’ Multimedia Event Reporters Society (SMERS) shall be a university, campus-based student organization, aiming to involve the students in any school event interview and documenting any school activities with permission of the school authorities. The student organization will enhance their communication skills in terms of reporting, interviewing, and acting skills for making short film documentaries and develop their skills for creating video documentation in every school activities.</p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>TUP Foundation Week</h1>
                <p>December 18 - 21, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at 
                        condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi 
                        nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada 
                        augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed 
                        elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/SMERS/MSERS3.jpg" alt="cyc 1">
                        <img src="static/Projects/SMERS/SMERS1.jpg" alt="cyc 2">
                        <img src="static/Projects/SMERS/SMERS2.jpg" alt="cyc 3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, 
                        id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum 
                        eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut 
                        pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, 
                        auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="SMERS">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
STUP = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>Sulong TUP - Manila</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/SulongGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/Missing.png" alt="pres-pic">
                <div>
                    <strong>Arabella Mae M. Aduviso</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>Sulong TUP's Vision</h2>
                    <p>Aliquam sed elit ex. Quisque sit amet fermentum diam. In posuere, mauris vel mattis efficitur, eros ipsum malesuada purus, id ornare velit arcu id nunc. Nunc quis dapibus nisl, a tempus lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer mi purus, ornare quis efficitur id, tempor eu arcu. Ut dapibus rhoncus nisl, et finibus mauris.</p>
                    <h2>Sulong TUP's Mission</h2>
                    <p>Maecenas finibus, nisl vitae interdum laoreet, lorem tortor hendrerit leo, vel pellentesque tellus ligula quis magna. Donec tristique purus massa, ac faucibus enim ultrices vel. Mauris quam urna, sodales non fermentum nec, pharetra tempor ligula. Vestibulum tempor tellus quis vehicula tristique. Etiam augue arcu, eleifend ac augue vitae, tristique sollicitudin orci. Donec auctor tincidunt arcu vel aliquet. Curabitur est mi, pulvinar eu porta ac, consequat at libero. Etiam sit amet magna sed mi ornare congue a a arcu.</p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>No events so far.</h1>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="STUP">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
TUPIVC = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>TUP Institute for Visual Communication</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/TUP-IVCGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/Missing.png" alt="pres-pic">
                <div>
                    <strong>Hannah D. Gozon</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>TUP-IVC's Vision</h2>
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie.
                        Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie
                    </p>
                    <h2>TUP-IVC's Mission</h2>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi</p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>TUP IVC's Hulaween 2024</h1>
                <p>November 6, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/TUP-IVC/IVC1.jpg" alt="D 1">
                        <img src="static/Projects/TUP-IVC/IVC2.jpg" alt="D 2">
                        <img src="static/Projects/TUP-IVC/IVC3.jpg" alt="D 3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="TUPIVC">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
TUPPAW = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>TUP Compassionate Partners for Animal Welfare and Nurturing Union</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/PUSAGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/Missing.png" alt="pres-pic">
                <div>
                    <strong>Frances Desiree D. Ete</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>TUP ComPAWnion's Vision</h2>
                    <p>Maecenas finibus, nisl vitae interdum laoreet, lorem tortor hendrerit leo, vel pellentesque tellus ligula quis magna. Donec tristique purus massa, ac faucibus enim ultrices vel. Mauris quam urna, sodales non fermentum nec, pharetra tempor ligula. Vestibulum tempor tellus quis vehicula tristique. Etiam augue arcu, eleifend ac augue vitae, tristique sollicitudin orci. Donec auctor tincidunt arcu vel aliquet. Curabitur est mi, pulvinar eu porta ac, consequat at libero. Etiam sit amet magna sed mi ornare congue a a arcu.</p>
                    <h2>TUP ComPAWnion's Mission</h2>
                    <p>Nullam pulvinar odio ac leo volutpat, sed convallis eros pretium. Suspendisse vel nibh sem. Maecenas suscipit, tellus quis eleifend venenatis, neque magna placerat arcu, a auctor eros nunc ut nisi. Aenean varius eros vitae efficitur posuere. Quisque semper pretium lorem non facilisis. Maecenas finibus turpis sit amet elementum venenatis.</p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>TUP Foundation Week</h1>
                <p>December 18 - 21, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/PUSA/PUSA1.jpg" alt="bol1">
                        <img src="static/Projects/PUSA/PUSA2.jpg" alt="bol2">
                        <img src="static/Projects/PUSA/PUSA3.jpg" alt="bol3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="TUPPAW">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
    
TUPDB = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>TUP Dugong Bughaw</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/TUPDBGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/Missing.png" alt="pres-pic">
                <div>
                    <strong>CJ Ken F. Lara</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>TUP DB's Vision</h2>
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at 
                        condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi 
                        nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <h2>TUP DB's Mission</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada 
                        augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed 
                        elementum dui elit, non consectetur enim imperdiet sed.</p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>TUP Foundation Week</h1>
                <p>December 18 - 21, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at 
                        condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi 
                        nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada 
                        augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed 
                        elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/TUP-DB/DB1.jpg" alt="cyc 1">
                        <img src="static/Projects/TUP-DB/DB2.jpg" alt="cyc 2">
                        <img src="static/Projects/TUP-DB/DB3.jpg" alt="cyc 3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, 
                        id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum 
                        eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut 
                        pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, 
                        auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="TUPDB">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
TUPGEAR = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>TUP Gaming Enthusiat Association Ring</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/GEARGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/GEARPRES.jpg" alt="pres-pic">
                <div>
                    <strong>Mari Nicolette Roldan</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>TUP GEAR's Vision</h2>
                    <p>To bring together a diverse group of bona fide students from the Technological University of the Philippines - Manila who share an interest in a wide variety of video games, whether on consoles, computers, or mobile devices. Our goal is to become an organization that fosters close relationships within the community, encompassing both recreational and competitive gaming.</p>
                    <h2>TUP GEAR's Mission</h2>
                    <p>To facilitate a student-led social community that collaborates to push Gaming and Esports into mainstream acceptance. We aim to educate students on the appreciation of video games as a form of art.</p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>TUP Foundation Week</h1>
                <p>December 18 - 21, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/GEAR/GEAR1.jpg" alt="D 1">
                        <img src="static/Projects/GEAR/GEAR2.jpg" alt="D 2">
                        <img src="static/Projects/GEAR/GEAR3.jpg" alt="D 3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="TUPGEAR">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
TUPGB = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>Grayhawks Robotics</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/GRAYBOTSGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/Missing.png" alt="pres-pic">
                <div>
                    <strong>Raine Francesca Maximo</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>TUP GRAYBOTS's Vision</h2>
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, 
                        id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie.</p>
                    <h2>TUP GRAYBOTS's Mission</h2>
                    <p>liquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut 
                        pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, 
                        auctor vitae nisi.</p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>TUP Foundation Week</h1>
                <p>December 18 - 21, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at 
                        condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi 
                        nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada 
                        augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed 
                        elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/GRAYBOTS/GB1.jpg" alt="cyc 1">
                        <img src="static/Projects/GRAYBOTS/GB2.jpg" alt="cyc 2">
                        <img src="static/Projects/GRAYBOTS/GB3.jpg" alt="cyc 3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, 
                        id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum 
                        eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut 
                        pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, 
                        auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="TUPGB">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
TUPMRC = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>TUP Manila Red Cross Youth</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/RCYGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/RCYPRES.jpg" alt="pres-pic">
                <div>
                    <strong>Jaeleigh Mavise P. Sulit</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>TUP-RCY's Vision</h2>
                    <p>
                        The TUPM-RCY acts locally for the National Youth 
                        Council (NYC) of the PRC, to implement, conduct, 
                        formulate, promote, disseminate and evaluate 
                        services and activities within the territory, 
                        under its jurisdiction in conformity with the charter, 
                        policies and regulations of the PRC. 
                    </p>
                    
                    <h2>TUP-RCY's Mission</h2>
                    <p>
                        The basic aim of the TUPM-RCY is to work within 
                        the Philippine Red Cross-Manila Chapter, to develop 
                        the youth in the spirit of humanitarianism and 
                        social service by giving them opportunities to 
                        participate in relevant Red Cross activities within 
                        the framework of the organization.
                    </p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>Blood Letting Activity</h1>
                <p>October 18, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/TUP-RCY/RCY1.jpg" alt="D 1">
                        <img src="static/Projects/TUP-RCY/RCY2.jpg" alt="D 2">
                        <img src="static/Projects/TUP-RCY/RCY3.jpg" alt="D 3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="TUPMRC">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
TUPTG = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>TUP Tech Guild</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/TGGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/Missing.png" alt="pres-pic">
                <div>
                    <strong>Ron Joshua H. Ochoa</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>TUP TECH GUILD's Vision</h2>
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at 
                        condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi 
                        nunc sollicitudin odio, sed lobortis nulla est non erat.Fusce quis sem a elit consequat tempor. 
                        Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi 
                        nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <h2>TUP TECH GUILD's Mission</h2>
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at 
                        condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi 
                        nunc sollicitudin odio, sed lobortis nulla est non erat.Fusce quis sem a elit consequat tempor. Nam efficitur sem at 
                        condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi 
                        nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>Accreditation</h1>
                <p>October 17, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at 
                        condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi 
                        nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada 
                        augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed 
                        elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/TECH GUILD/TG1.jpg" alt="cyc 1">
                        <img src="static/Projects/TECH GUILD/TG2.jpg" alt="cyc 2">
                        <img src="static/Projects/TECH GUILD/TG3.jpg" alt="cyc 3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, 
                        id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum 
                        eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut 
                        pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, 
                        auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="TUPTG">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
TUPDOST = ''' 
        <div class="conts" id="org">
            <div class="head">
                <h1>DOST Scholars' Club</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/DOSTGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/DOSTPRES.jpg" alt="pres-pic">
                <div>
                    <strong>Emmanuel M. Lungay</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>DOST Scholars' Club's Vision</h2>
                    <p>The TUP-M DOST Scholars' Club aspires to establish itself
                        as a prominent hub of intellectual and moral development 
                        within the univversity. The unwavering dedication to the 
                        principles of servant leadership, professional excellence,
                        and social responsiblity shal empower the scholars to emerge
                        as fervent, determined, and compassionate individuals dedicated 
                        to the service of God, the nation, the community, the institution, 
                        and their families
                    </p>

                    <h2>DOST Scholars' Club's Mission</h2>
                    <p>
                        TUP-M DOST Scholars' Club will fulfill its vision by:<br>
                        1. Cultivating a vibrant and cohesive community amongst DOST Scholars 
                        enrolled at the Technological University of the Philippines - Manila. <br>
                        2. Implementing innovating initiatives to fster the holistic growth of the scholars.<br>
                        3. Upholding the core values of serveant leadership, professional excellence, 
                        and social responsibility, as an integral part of our commitment to the nation.
                    </p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>TUP Foundation Week</h1>
                <p>December 18 - 21, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/DOST/DOST1.jpg" alt="D 1">
                        <img src="static/Projects/DOST/DOST2.jpg" alt="D 2">
                        <img src="static/Projects/DOST/DOST3.jpg" alt="D 3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="TUPDOST">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
WBCC = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>World Book Crossing Club - Philippines</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/WBCCGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/WBBCPPRES.jpg" alt="pres-pic">
                <div>
                    <strong>John Lawrence a. Francisco</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>WBCCP's Vision</h2>
                    <p>
                        Foster a global community bound by the love of literature, 
                        the World Book Crossing Club envisions a world where books 
                        transcend boundaries, connecting people across cultures, 
                        sparking imagination, and inspiring positive change. 
                    </p>
                    
                    <h2>WBCCP's Mission</h2>
                    <p>
                        Promote the joy of reading and the exchange of ideas by creating 
                        a dynamic network of individuals who share and release books 
                        as they journey through the hands of readers worldwide. 
                        Through our shared love of books, we aim to cultivate a sense of 
                        community, promote literacy, and contribute to the collective 
                        enrichment of global knowledge and understanding. 
                    </p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>TUP Foundation Week</h1>
                <p>December 18 - 21, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/WBCCP/WBCCP1.jpg" alt="bol1">
                        <img src="static/Projects/WBCCP/WBCC3.jpg" alt="bol2">
                        <img src="static/Projects/WBCCP/WBCCP2.jpg" alt="bol3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="WBCC">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        
YEGD = '''
        <div class="conts" id="org">
            <div class="head">
                <h1>YOUth EMPOWERing gender and Development</h1>
            </div>

            <div class="GP">
                <img src="static/Group Photo/YEGADGP.jpg" alt="CYCGP1">
            </div>

            <div class="pres-info">
                <img src="static/Presidents/Missing.png" alt="pres-pic">
                <div>
                    <strong>Rose Mae R. Umali</strong><br>
                    President
                </div>
            </div>

            <div class="section">
                <h1>Vision & Mission</h1>
                <div class="vision-mision">
                    <h2>YEGAD's Vision</h2>
                    <p>Maecenas finibus, nisl vitae interdum laoreet, lorem tortor hendrerit leo, vel pellentesque tellus ligula quis magna. Donec tristique purus massa, ac faucibus enim ultrices vel. Mauris quam urna, sodales non fermentum nec, pharetra tempor ligula. Vestibulum tempor tellus quis vehicula tristique. Etiam augue arcu, eleifend ac augue vitae, tristique sollicitudin orci. Donec auctor tincidunt arcu vel aliquet. Curabitur est mi, pulvinar eu porta ac, consequat at libero. Etiam sit amet magna sed mi ornare congue a a arcu.</p>
                    <h2>YEGAD's Mission</h2>
                    <p>Aliquam sed elit ex. Quisque sit amet fermentum diam. In posuere, mauris vel mattis efficitur, eros ipsum malesuada purus, id ornare velit arcu id nunc. Nunc quis dapibus nisl, a tempus lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer mi purus, ornare quis efficitur id, tempor eu arcu. Ut dapibus rhoncus nisl, et finibus mauris.</p>
                </div>
            </div>

            <div class="container">
                <h2>Projects and Achievments</h2>
            </div>

            <div class="container">
                <h1>Seminar on Mental Health Awareness regarding Violence Against Women and Children</h1>
                <p>November 29, 2024</p>
                <div class="content">
                    <p>Fusce quis sem a elit consequat tempor. Nam efficitur sem at condimentum sagittis. Vivamus lobortis, mi vitae convallis condimentum, nisi nunc sollicitudin odio, sed lobortis nulla est non erat.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada augue eu lacinia pharetra. </span> Curabitur lobortis at arcu quis ornare. Sed elementum dui elit, non consectetur enim imperdiet sed.</p>
                    
                    <div class="image-container">
                        <img src="static/Projects/YEGAD/YEGAD1.jpg" alt="bol1">
                        <img src="static/Projects/YEGAD/YEGAD2.jpg" alt="bol2">
                        <img src="static/Projects/YEGAD/YEGAD3.jpg" alt="bol3">
                    </div>
        
                    <p>Nullam tincidunt vestibulum lorem ac maximus. Sed tempus libero lacus, id euismod erat ultrices sed. Integer fringilla accumsan massa vitae molestie</p>
                    <p> Donec dapibus ipsum quis massa convallis sodales. Ut ut nulla mi. Vestibulum eget lacus eget nisl euismod fermentum. Nulla vehicula erat vitae molestie posuere.</p>
                    <p>Aliquam nec mauris sed quam malesuada volutpat. Fusce iaculis finibus porta. Ut pharetra purus a ex euismod eleifend. Nunc dolor nulla, tincidunt vel euismod eu, auctor vitae nisi.</p>
                </div>
            </div>
        </div>

        <form action="/apply" method="post" id='applyForm'>
            <button type="submit" name="org" value="YEGD">Apply Now!</button>
        </form>
        
        <div class="footer"></div>
    '''
        