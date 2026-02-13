from django.shortcuts import render
from django.http import HttpResponse

# اولین ویو ساده
def home_page(request):
    """صفحه اصلی سایت"""
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>اولین سایت جنگو من</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                padding: 40px;
                max-width: 800px;
                width: 100%;
                text-align: center;
            }
            
            h1 {
                color: #333;
                margin-bottom: 20px;
                font-size: 2.5em;
            }
            
            h2 {
                color: #667eea;
                margin: 30px 0 10px 0;
                font-size: 1.8em;
            }
            
            .highlight {
                color: #764ba2;
                font-weight: bold;
            }
            
            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin: 30px 0;
            }
            
            .feature-card {
                background: #f8f9fa;
                border-radius: 10px;
                padding: 20px;
                border: 2px solid #e9ecef;
                transition: all 0.3s ease;
            }
            
            .feature-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                border-color: #667eea;
            }
            
            .feature-card h3 {
                color: #495057;
                margin-bottom: 10px;
            }
            
            .btn {
                display: inline-block;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 15px 40px;
                border-radius: 50px;
                text-decoration: none;
                font-weight: bold;
                margin: 10px;
                border: none;
                cursor: pointer;
                font-size: 1.1em;
                transition: all 0.3s ease;
            }
            
            .btn:hover {
                transform: scale(1.05);
                box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
            }
            
            .badge {
                background: #28a745;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.9em;
                margin-left: 10px;
            }
            
            .footer {
                margin-top: 40px;
                color: #6c757d;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 موفق شدی! <span class="highlight">اولین سایت جنگو</span> را ساختی</h1>
            
            <div class="badge">زنده و فعال</div>
            
            <p style="color: #666; margin: 20px 0; font-size: 1.2em; line-height: 1.6;">
                خوش آمدی به دنیای حرفه‌ای توسعه وب! این صفحه با <strong>Django</strong> و <strong>Python</strong> ساخته شده است.
            </p>
            
            <h2>🚀 قابلیت‌های سایت:</h2>
            
            <div class="features">
                <div class="feature-card">
                    <h3>✅ بک‌اند قدرتمند</h3>
                    <p>پایتون + جنگو = بهترین ترکیب برای توسعه وب</p>
                </div>
                
                <div class="feature-card">
                    <h3>📱 ریسپانسیو</h3>
                    <p>سایت در همه دستگاه‌ها به خوبی نمایش داده می‌شود</p>
                </div>
                
                <div class="feature-card">
                    <h3>⚡ سریع و ایمن</h3>
                    <p>امنیت بالا و سرعت اجرای عالی</p>
                </div>
            </div>
            
            <div style="margin: 30px 0;">
                <h2>🎯 قدم‌های بعدی:</h2>
                <p style="color: #666; margin: 15px 0;">حالا می‌توانی:</p>
                
                <div style="text-align: left; max-width: 500px; margin: 0 auto;">
                    <p>1. 🔗 صفحات جدید اضافه کنی</p>
                    <p>2. 🗄️ پایگاه داده بسازی</p>
                    <p>3. 🎨 تمپلیت HTML واقعی استفاده کنی</p>
                    <p>4. 👤 سیستم کاربری اضافه کنی</p>
                </div>
            </div>
            
            <div style="margin: 40px 0;">
                <button class="btn" onclick="alert('اولین کلیک در سایت جنگو! 🎉')">
                    🎯 تست کلیک
                </button>
                
                <a href="/admin" class="btn" style="background: #343a40;">
                    🛠️ پنل مدیریت
                </a>
            </div>
            
            <div class="footer">
                <p>ساخته شده با ❤️ در جلسه آموزش جنگو</p>
                <p>سرور در حال اجرا روی: 127.0.0.1:8000</p>
            </div>
            <div class="nav-links">
                <a href="/services/">🛠️ خدمات</a>
                <a href="/about/">ℹ️ درباره ما</a>
                <a href="/contact/">📞 تماس</a>
            </div>
        </div>
        
        <script>
            // یک انیمیشن ساده برای کارت‌ها
            document.addEventListener('DOMContentLoaded', function() {
                const cards = document.querySelectorAll('.feature-card');
                cards.forEach((card, index) => {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    
                    setTimeout(() => {
                        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, index * 200);
                });
            });
        </script>
    </body>
    </html>
    """)


def about_page(request):
    """صفحه درباره ما"""
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>درباره ما</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #f5f7fa;
                margin: 0;
                padding: 20px;
                color: #333;
            }
            
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            
            h1 {
                color: #4a5568;
                border-bottom: 3px solid #667eea;
                padding-bottom: 10px;
            }
            
            .back-btn {
                display: inline-block;
                background: #667eea;
                color: white;
                padding: 10px 25px;
                border-radius: 5px;
                text-decoration: none;
                margin-top: 20px;
            }
            
            .tech-list {
                list-style-type: none;
                padding: 0;
            }
            
            .tech-list li {
                background: #f8f9fa;
                margin: 10px 0;
                padding: 15px;
                border-radius: 8px;
                border-right: 5px solid #667eea;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📖 درباره این پروژه</h1>
            
            <p style="line-height: 1.8; font-size: 1.1em;">
                این پروژه اولین گام تو در دنیای توسعه وب با جنگو است. 
                ما قصد داریم یک پورتفولیو کامل و سیستم آموزش برنامه‌نویسی بسازیم.
            </p>
            
            <h2>🛠️ تکنولوژی‌های استفاده شده:</h2>
            
            <ul class="tech-list">
                <li><strong>Python 3.12</strong> - زبان برنامه‌نویسی اصلی</li>
                <li><strong>Django 4.2</strong> - فریم‌ورک وب قدرتمند</li>
                <li><strong>HTML5 & CSS3</strong> - ساختار و استایل صفحات</li>
                <li><strong>JavaScript</strong> - تعاملات سمت کلاینت</li>
            </ul>
            
            <h2>🎯 اهداف پروژه:</h2>
            
            <p>1. نمایش پروژه‌های برنامه‌نویسی<br>
               2. آموزش برنامه‌نویسی به دیگران<br>
               3. ایجاد سیستم عضویت و درآمدزایی<br>
               4. تمرین بهترین متدهای توسعه نرم‌افزار</p>
            <div class="nav-links">
                <a href="/">🏠 صفحه اصلی</a>
                <a href="/contact/">📞 تماس</a>
                <a href="/services/">🛠️ خدمات</a>
            </div>
            <a href="/" class="back-btn">← بازگشت به صفحه اصلی</a>
        </div>
    </body>
    </html>
    """)


def contact_page(request):
    """صفحه تماس با ما"""
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>تماس با ما</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                margin: 0;
                padding: 20px;
                min-height: 100vh;
            }
            
            .container {
                max-width: 600px;
                margin: 40px auto;
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 15px 40px rgba(0,0,0,0.15);
            }
            
            h1 {
                color: #2d3748;
                text-align: center;
                margin-bottom: 30px;
            }
            
            .form-group {
                margin-bottom: 25px;
            }
            
            label {
                display: block;
                margin-bottom: 8px;
                color: #4a5568;
                font-weight: 600;
            }
            
            input, textarea {
                width: 100%;
                padding: 12px;
                border: 2px solid #e2e8f0;
                border-radius: 8px;
                font-size: 16px;
                transition: border-color 0.3s;
            }
            
            input:focus, textarea:focus {
                outline: none;
                border-color: #667eea;
            }
            
            textarea {
                height: 150px;
                resize: vertical;
            }
            
            .btn {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 15px 40px;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                width: 100%;
                transition: transform 0.3s;
            }
            
            .btn:hover {
                transform: translateY(-2px);
            }
            
            .links {
                text-align: center;
                margin-top: 30px;
            }
            
            .links a {
                color: #667eea;
                text-decoration: none;
                margin: 0 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📞 تماس با ما</h1>
            
            <form id="contactForm">
                <div class="form-group">
                    <label for="name">نام و نام خانوادگی:</label>
                    <input type="text" id="name" placeholder="مثلا: علی محمدی" required>
                </div>
                
                <div class="form-group">
                    <label for="email">ایمیل:</label>
                    <input type="email" id="email" placeholder="example@email.com" required>
                </div>
                
                <div class="form-group">
                    <label for="subject">موضوع:</label>
                    <input type="text" id="subject" placeholder="مثلا: سوال درباره آموزش‌ها" required>
                </div>
                
                <div class="form-group">
                    <label for="message">پیام:</label>
                    <textarea id="message" placeholder="پیام خود را اینجا بنویسید..." required></textarea>
                </div>
                
                <button type="submit" class="btn">📤 ارسال پیام</button>
            </form>
            
            <div class="links">
                <a href="/">🏠 صفحه اصلی</a> | 
                <a href="/about/">ℹ️ درباره ما</a>
            </div>
        </div>
            <div class="nav-links">
                <a href="/">🏠 صفحه اصلی</a>
                <a href="/about/">ℹ️ درباره ما</a>
                <a href="/services/">🛠️ خدمات</a>
            </div>
        <script>
            document.getElementById('contactForm').addEventListener('submit', function(e) {
                e.preventDefault();
                
                const name = document.getElementById('name').value;
                alert(`پیام شما ارسال شد ${name} عزیز! (این یک دمو است)`);
                
                // ریست فرم
                this.reset();
            });
        </script>
    </body>
    </html>
    """)
    

def services_page(request):
    """صفحه خدمات"""
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>خدمات ما</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #f0f2f5;
                margin: 0;
                padding: 20px;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
            }
            
            h1 {
                text-align: center;
                color: #2d3748;
                margin-bottom: 40px;
            }
            
            .services-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
            }
            
            .service-card {
                background: white;
                border-radius: 10px;
                padding: 30px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                transition: transform 0.3s ease;
            }
            
            .service-card:hover {
                transform: translateY(-10px);
            }
            
            .service-icon {
                font-size: 2.5em;
                text-align: center;
                margin-bottom: 20px;
            }
            
            .service-title {
                color: #4a5568;
                text-align: center;
                margin-bottom: 15px;
            }
            
            .service-desc {
                color: #718096;
                line-height: 1.6;
                text-align: center;
            }
            
            .btn {
                display: block;
                width: 200px;
                margin: 30px auto;
                padding: 12px;
                background: #4299e1;
                color: white;
                text-align: center;
                text-decoration: none;
                border-radius: 5px;
            }
            
            .nav-links {
                text-align: center;
                margin-top: 40px;
            }
            
            .nav-links a {
                margin: 0 15px;
                color: #4a5568;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🛠️ خدمات ما</h1>
            
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">💻</div>
                    <h3 class="service-title">توسعه وب سایت</h3>
                    <p class="service-desc">
                        طراحی و توسعه وب‌سایت‌های حرفه‌ای با جنگو و پایتون
                    </p>
                </div>
                
                <div class="service-card">
                    <div class="service-icon">🎓</div>
                    <h3 class="service-title">آموزش برنامه‌نویسی</h3>
                    <p class="service-desc">
                        آموزش از صفر تا صد پایتون، جنگو و توسعه وب
                    </p>
                </div>
                
                <div class="service-card">
                    <div class="service-icon">🤖</div>
                    <h3 class="service-title">هوش مصنوعی</h3>
                    <p class="service-desc">
                        توسعه مدل‌های هوش مصنوعی و یادگیری ماشین
                    </p>
                </div>
            </div>
            
            <a href="/contact/" class="btn">📞 درخواست خدمت</a>
            
            <div class="nav-links">
                <a href="/">🏠 صفحه اصلی</a>
                <a href="/about/">ℹ️ درباره ما</a>
                <a href="/contact/">📞 تماس</a>
            </div>
        </div>
    </body>
    </html>
    """)