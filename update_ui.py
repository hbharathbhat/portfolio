import re

file_path = r"d:\bharath\portfolio\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace variables
html = html.replace("""        /* --- CSS VARIABLES & RESET --- */
        :root {
            --primary: #2c3e50;
            /* Dark Blue/Grey */
            --secondary: #009999;
            /* Siemens Teal */
            --accent: #e74c3c;
            /* Red Accent */
            --light-bg: #f4f7f6;
            --white: #ffffff;
            --text-main: #333333;
            --text-light: #666666;
            --card-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
            /* Glassmorphism shadow */
        }""", """        /* --- CSS VARIABLES & RESET --- */
        :root {
            --primary: #2c3e50;
            --secondary: #009999;
            --accent: #e74c3c;
            --light-bg: #f4f7f6;
            --white: #ffffff;
            --text-main: #333333;
            --text-light: #666666;
            --text-header: #2c3e50;
            --card-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
            --bg-color: #f4f7f6;
            --nav-bg: rgba(255, 255, 255, 0.95);
            --nav-text: #333333;
            --card-bg: rgba(255, 255, 255, 0.95);
            --card-bg-hover: #ffffff;
            --tag-bg: #eef2f7;
            --tag-text: var(--text-main);
            --form-bg: rgba(255, 255, 255, 0.95);
            --footer-bg: rgba(244, 247, 246, 0.95);
            --footer-text: #333333;
            --cert-border: #2c3e50;
        }

        [data-theme="dark"] {
            --primary: #48c9b0;
            --secondary: #48c9b0;
            --accent: #ff7675;
            --light-bg: #111827;
            --white: #1f2937;
            --text-main: #f3f4f6;
            --text-light: #9ca3af;
            --text-header: #ffffff;
            --card-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
            --bg-color: #030712;
            --nav-bg: rgba(17, 24, 39, 0.95);
            --nav-text: #ffffff;
            --card-bg: rgba(31, 41, 55, 0.95);
            --card-bg-hover: #374151;
            --tag-bg: #374151;
            --tag-text: #f3f4f6;
            --form-bg: rgba(31, 41, 55, 0.95);
            --footer-bg: rgba(17, 24, 39, 0.95);
            --footer-text: #f3f4f6;
            --cert-border: #48c9b0;
        }""")

html = html.replace("""        /* --- SPACE BACKGROUND CANVAS --- */
        #space-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            /* Places it behind everything */
            background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
        }""", """        /* --- VLSI CANVAS --- */
        #vlsi-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: var(--bg-color);
            transition: background 0.5s ease;
        }""")

html = html.replace("""        nav {
            background-color: rgba(44, 62, 80, 0.95);
            /* Slight transparency */
            backdrop-filter: blur(5px);
            color: white;
            padding: 1rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }""", """        nav {
            background-color: var(--nav-bg);
            /* Slight transparency */
            backdrop-filter: blur(5px);
            color: var(--nav-text);
            padding: 1rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }""")

html = html.replace("""        .logo span {
            color: white;
        }""", """        .logo span {
            color: var(--nav-text);
        }""")

html = html.replace("""        .nav-links li:hover,
        .nav-links li.active {
            background-color: rgba(255, 255, 255, 0.1);
            color: var(--secondary);
        }""", """        .nav-links li:hover,
        .nav-links li.active {
            background-color: var(--tag-bg);
            color: var(--secondary);
        }""")

html = html.replace("""        .menu-toggle {
            display: none;
            cursor: pointer;
            font-size: 1.5rem;
            color: white;
        }""", """        .menu-toggle {
            display: none;
            cursor: pointer;
            font-size: 1.5rem;
            color: var(--nav-text);
        }""")

html = html.replace("""        h1 {
            color: var(--primary);
            margin-bottom: 0.5rem;
            font-size: 3rem;
            line-height: 1.2;
        }""", """        h1 {
            color: var(--text-header);
            margin-bottom: 0.5rem;
            font-size: 3rem;
            line-height: 1.2;
        }""")

html = html.replace("""        h2 {
            color: #ffffff;
            /* White text to stand out against space */
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
            font-size: 2rem;
            margin: 40px 0 20px 0;
            border-bottom: 3px solid var(--secondary);
            display: inline-block;
            padding-bottom: 5px;
        }""", """        h2 {
            color: var(--text-header);
            font-size: 2rem;
            margin: 40px 0 20px 0;
            border-bottom: 3px solid var(--secondary);
            display: inline-block;
            padding-bottom: 5px;
        }""")

html = html.replace("""        h3 {
            color: var(--primary);
            margin-bottom: 5px;
            font-size: 1.25rem;
            font-weight: 700;
        }""", """        h3 {
            color: var(--text-header);
            margin-bottom: 5px;
            font-size: 1.25rem;
            font-weight: 700;
        }""")

html = html.replace("""        .section-subtitle {
            font-size: 1.5rem;
            color: #ddd;
            /* Lighter text for subtitle against space */
            margin: 30px 0 15px 0;
            font-weight: 600;
            border-left: 4px solid var(--accent);
            padding-left: 10px;
        }""", """        .section-subtitle {
            font-size: 1.5rem;
            color: var(--text-light);
            margin: 30px 0 15px 0;
            font-weight: 600;
            border-left: 4px solid var(--accent);
            padding-left: 10px;
        }""")

html = html.replace("""        .hero {
            background: rgba(255, 255, 255, 0.92);
            /* Glass effect */""", """        .hero {
            background: var(--card-bg);
            /* Glass effect */""")

html = html.replace("""        .card {
            background: rgba(255, 255, 255, 0.95);
            /* Slight transparency */""", """        .card {
            background: var(--card-bg);
            /* Slight transparency */""")

html = html.replace("""        .card:hover {
            transform: translateY(-5px);
            background: #ffffff;
            /* Solid white on hover */""", """        .card:hover {
            transform: translateY(-5px);
            background: var(--card-bg-hover);
            /* Solid white on hover */""")

html = html.replace("""        .tag {
            display: inline-block;
            background: #eef2f7;
            color: var(--primary);""", """        .tag {
            display: inline-block;
            background: var(--tag-bg);
            color: var(--tag-text);""")

html = html.replace("""        .cert-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 20px;
            border-radius: 8px;
            box-shadow: var(--card-shadow);
            border-top: 4px solid var(--primary);
        }""", """        .cert-card {
            background: var(--card-bg);
            padding: 20px;
            border-radius: 8px;
            box-shadow: var(--card-shadow);
            border-top: 4px solid var(--cert-border);
        }""")

html = html.replace("""        .contact-container {
            max-width: 600px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);""", """        .contact-container {
            max-width: 600px;
            margin: 0 auto;
            background: var(--form-bg);""")

html = html.replace("""        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
            color: var(--primary);
        }""", """        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
            color: var(--text-header);
        }""")

html = html.replace("""        .form-control {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-family: inherit;
        }""", """        .form-control {
            width: 100%;
            padding: 12px;
            border: 1px solid var(--tag-bg);
            background: transparent;
            color: var(--text-main);
            border-radius: 5px;
            font-family: inherit;
        }""")

html = html.replace("""        footer {
            background-color: rgba(44, 62, 80, 0.95);
            color: white;""", """        footer {
            background-color: var(--footer-bg);
            color: var(--footer-text);""")

html = html.replace("""        .footer-links a {
            color: #ccc;""", """        .footer-links a {
            color: var(--footer-text);""")

html = html.replace("""            .nav-links {
                position: fixed;
                right: 0;
                top: 0;
                height: 100vh;
                width: 65%;
                /* Width of the drawer */
                background-color: var(--primary);""", """            .nav-links {
                position: fixed;
                right: 0;
                top: 0;
                height: 100vh;
                width: 65%;
                /* Width of the drawer */
                background-color: var(--nav-bg);""")

html = html.replace("""    <canvas id="space-canvas"></canvas>""", """    <canvas id="vlsi-canvas"></canvas>""")

html = html.replace("""        <div class="menu-toggle" onclick="toggleMenu()">
            <i class="fa-solid fa-bars"></i>
        </div>""", """        <div style="display: flex; align-items: center;">
            <div id="themeToggle" onclick="toggleTheme()" style="cursor: pointer; margin-right: 20px; font-size: 1.2rem; transition: 0.3s; color: var(--nav-text);">
                <i class="fa-solid fa-moon"></i>
            </div>
            <div class="menu-toggle" onclick="toggleMenu()">
                <i class="fa-solid fa-bars"></i>
            </div>
        </div>""")

new_js = """        /* --- THEME TOGGLE LOGIC --- */
        function toggleTheme() {
            const body = document.documentElement;
            const currentTheme = body.getAttribute('data-theme');
            const icon = document.querySelector('#themeToggle i');
            
            if (currentTheme === 'dark') {
                body.removeAttribute('data-theme');
                icon.className = 'fa-solid fa-moon';
                localStorage.setItem('theme', 'light');
            } else {
                body.setAttribute('data-theme', 'dark');
                icon.className = 'fa-solid fa-sun';
                localStorage.setItem('theme', 'dark');
            }
        }
        
        // Auto-check theme
        document.addEventListener('DOMContentLoaded', () => {
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                document.documentElement.setAttribute('data-theme', 'dark');
                document.querySelector('#themeToggle i').className = 'fa-solid fa-sun';
            }
        });

        /* --- VLSI CHIP BACKGROUND LOGIC --- */
        const canvas = document.getElementById('vlsi-canvas');
        const ctx = canvas.getContext('2d');

        function resize() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            if(nodes.length === 0) initNodes();
        }
        window.addEventListener('resize', resize);

        const nodes = [];
        let numNodes = 0;

        class Node {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.vx = (Math.random() - 0.5) * 0.5;
                this.vy = (Math.random() - 0.5) * 0.5;
                this.size = Math.random() * 2 + 1.5;
            }
            update() {
                this.x += this.vx;
                this.y += this.vy;
                if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
                if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
            }
            draw() {
                ctx.fillRect(this.x - this.size, this.y - this.size, this.size * 2, this.size * 2);
            }
        }

        function initNodes() {
            nodes.length = 0;
            numNodes = Math.floor((window.innerWidth * window.innerHeight) / 12000); 
            for (let i = 0; i < numNodes; i++) {
                nodes.push(new Node());
            }
        }

        resize();

        function drawVLSI() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            
            const nodeColor = isDark ? '#48c9b0' : '#009999';
            const lineColor = isDark ? 'rgba(72, 201, 176, 0.15)' : 'rgba(0, 153, 153, 0.15)';
            const pulseColor = isDark ? 'rgba(255, 118, 117, 0.8)' : 'rgba(231, 76, 60, 0.8)';
            
            ctx.fillStyle = nodeColor;
            
            nodes.forEach(node => {
                node.update();
                node.draw();
            });
            
            ctx.lineWidth = 1;
            for (let i = 0; i < nodes.length; i++) {
                for (let j = i + 1; j < nodes.length; j++) {
                    const cx = nodes[j].x - nodes[i].x;
                    const cy = nodes[j].y - nodes[i].y;
                    const dist = Math.sqrt(cx * cx + cy * cy);
                    
                    if (dist < 120) {
                        ctx.strokeStyle = lineColor;
                        ctx.beginPath();
                        ctx.moveTo(nodes[i].x, nodes[i].y);
                        
                        if (Math.abs(cx) > Math.abs(cy)) {
                            ctx.lineTo(nodes[j].x, nodes[i].y);
                        } else {
                            ctx.lineTo(nodes[i].x, nodes[j].y);
                        }
                        ctx.lineTo(nodes[j].x, nodes[j].y);
                        ctx.stroke();
                        
                        if(Math.random() > 0.995) {
                            ctx.fillStyle = pulseColor;
                            const t = Math.random();
                            let px, py;
                            if (Math.abs(cx) > Math.abs(cy)) {
                                if (t < 0.5) {
                                    px = nodes[i].x + cx * (t * 2);
                                    py = nodes[i].y;
                                } else {
                                    px = nodes[j].x;
                                    py = nodes[i].y + cy * ((t - 0.5) * 2);
                                }
                            } else {
                                if (t < 0.5) {
                                    px = nodes[i].x;
                                    py = nodes[i].y + cy * (t * 2);
                                } else {
                                    px = nodes[i].x + cx * ((t - 0.5) * 2);
                                    py = nodes[j].y;
                                }
                            }
                            ctx.fillRect(px - 1.5, py - 1.5, 3, 3);
                            ctx.fillStyle = nodeColor;
                        }
                    }
                }
            }
            requestAnimationFrame(drawVLSI);
        }

        drawVLSI();"""

import re
html = re.sub(r'\s*/\* --- SPACE BACKGROUND LOGIC --- \*/.*?(?=\s*</script>)', '\n' + new_js, html, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated successfully")
