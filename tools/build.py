# Run: python3 tools/build.py   (from the site folder). Edit tools/data.json to add FAQs/blog posts.
import json,os,html,shutil
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=json.load(open(os.path.join(R,'tools','data.json'),encoding='utf-8'))
U='https://jasujahosiery.com'
E=html.escape
PH1,PH2,MAIL='+919358583300','+918791907779','info@jasujahosiery.com'
MAP='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3456.221421784885!2d77.54783457555102!3d29.973065974959624!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390eeb49363e3c87%3A0x78506a50a88eac6a!2sJasuja%20Hosiery!5e0!3m2!1sen!2sin!4v1791187238694!5m2!1sen!2sin'
NAV=[('/','Home'),('/products/','Products'),('/brands/','Brands'),('/about/','About'),('/faq/','FAQ'),('/blog/','Blog'),('/contact/','Contact')]
ORG={"@context":"https://schema.org","@type":"Organization","name":"Jasuja Hosiery","url":U,"foundingDate":"1976","email":MAIL,"telephone":["+91-9358583300","+91-8791907779"],"description":"Manufacturer and trader of hosiery goods, thermal wear and cotton apparel in India since 1976.","brand":[{"@type":"Brand","name":n} for n in ["JH Thermals","Real Quilt"]]}
def ld(o): return '<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False)+'</script>'
def page(path,title,desc,body,extra='',typ='website'):
    nav=''.join('<a href="%s"%s>%s</a>'%(h,' class="on"' if (h==path or (h!='/' and path.startswith(h))) else '',n) for h,n in NAV)
    url=U+path
    out='''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s</title><meta name="description" content="%s"><link rel="canonical" href="%s">
<meta property="og:type" content="%s"><meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:url" content="%s"><meta property="og:site_name" content="Jasuja Hosiery"><meta name="twitter:card" content="summary">
<meta name="theme-color" content="#8B6B00">
<link rel="icon" href="data:image/svg+xml,&lt;svg xmlns=%%27http://www.w3.org/2000/svg%%27 viewBox=%%270 0 100 100%%27&gt;&lt;text y=%%27.9em%%27 font-size=%%2790%%27&gt;🧵&lt;/text&gt;&lt;/svg&gt;">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">%s</head><body>
<nav><a class="logo" href="/">JH<span>.</span></a><div class="links">%s</div></nav>
<main>%s</main>
<footer><b>JASUJA HOSIERY</b> &nbsp;·&nbsp; INDIA &nbsp;·&nbsp; SINCE 1976<br><a href="tel:%s">+91 93585 83300</a> · <a href="mailto:%s">%s</a></footer>
</body></html>'''%(E(title),E(desc),url,typ,E(title),E(desc),url,extra,nav,body,PH1,MAIL,MAIL)
    d=os.path.join(R,path.strip('/'));os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(out)
def head(eb,h,sub=''): return '<div class="wrap head"><p class="eyebrow">%s</p><h1 style="font-size:clamp(34px,6vw,60px);margin:10px 0">%s</h1>%s</div>'%(eb,h,'<p class="lead" style="margin:0;text-align:left">%s</p>'%sub if sub else '')
def card(t,h,p,href=None):
    c='<span class="t">%s</span><h3>%s</h3><p>%s</p>'%(t,h,p) if t else '<h3>%s</h3><p>%s</p>'%(h,p)
    return '<a class="card" href="%s">%s</a>'%(href,c) if href else '<div class="card">%s</div>'%c
CTA='<div class="btns"><a class="btn" href="https://wa.me/919358583300">WhatsApp us</a><a class="btn o" href="/contact/">Contact</a></div>'
MFG=['JH Thermals','Real Quilt','OEM']
TRD=['White Rose','Array','Sweet Touch','PaceOne','Tropical Rainwear','Pinklush','Kidley','Melini']
# HOME
page('/','Jasuja Hosiery | Hosiery, Thermal Wear & Cotton Apparel Manufacturer Since 1976','Jasuja Hosiery manufactures and trades hosiery goods, thermal wear and cotton apparel in India since 1976. Brands: JH Thermals, Real Quilt, White Rose, Array and more.',
'''<div class="wrap hero"><p class="eyebrow">Since 1976</p><h1>JASUJA</h1><div class="bar">HOSIERY</div>
<p class="lead">Manufacturers and traders of hosiery, thermal wear and cotton apparel. Trusted across India for nearly fifty years.</p>
<div class="btns"><a class="btn" href="/products/">Explore products</a><a class="btn o" href="/contact/">Get in touch</a></div></div>
<div class="wrap sec"><div class="stats"><div><b>1976</b><span>Established</span></div><div><b>3</b><span>Product families</span></div><div><b>10+</b><span>Brands</span></div></div></div>
<div class="wrap sec"><h2>We make. We trade.</h2><div class="grid">%s%s</div></div>
<div class="wrap sec"><h2>From our blog</h2><div class="grid post">%s</div></div>'''%(
card('Manufacturing','Our own brands','JH Thermals, Real Quilt and OEM production for partners.','/brands/'),
card('Trading','Brands we trust','White Rose, Array, Sweet Touch, PaceOne and many more.','/brands/'),
''.join(card('',p['t'],E(p['p'][0]),'/blog/%s/'%p['s']) for p in D['posts'][:3])),ld(ORG))
# PRODUCTS
page('/products/','Hosiery, Thermal Wear & Cotton Apparel | Jasuja Hosiery','Explore Jasuja Hosiery products: all types of hosiery goods, JH Thermals in sizes 36 to 90, and comfortable cotton apparel for men, women and kids.',
head('Products','Everything in hosiery.')+'''<div class="wrap"><div class="grid" style="margin-top:0">%s%s%s</div></div>
<div class="wrap sec" style="margin-top:60px"><p class="eyebrow">JH Thermals</p><h2>Sizes 36 – 90</h2>
<p class="lead" style="margin:14px 0 0;text-align:left">Machine wash at 30°. Do not bleach. Do not iron. Read <a href="/blog/how-to-wash-thermals/" style="color:var(--gold)">how to wash thermals</a>.</p>%s</div>'''%(
card('01','Hosiery goods','All types of hosiery goods for men, women and kids.'),card('02','Thermal wear','JH Thermals for the whole family, in sizes 36 to 90.'),card('03','Cotton apparel','Comfortable everyday cotton wear.'),
'<div class="btns" style="justify-content:flex-start">%s</div>'%'<a class="btn" href="/contact/">Enquire now</a>'))
# BRANDS
chips=lambda l,g='':''.join('<span class="chip%s">%s</span>'%(g,E(x)) for x in l)
page('/brands/','Brands We Manufacture & Trade | Jasuja Hosiery','Jasuja Hosiery manufactures JH Thermals, Real Quilt and OEM, and trades in White Rose, Array, Sweet Touch, PaceOne, Tropical Rainwear, Pinklush, Kidley and Melini.',
head('Brands','Made by us. Trusted by us.')+'<div class="wrap"><p class="sub">Brands we manufacture</p><div class="chips">%s<span class="chip">and many more</span></div><p class="sub">Brands we trade in</p><div class="chips">%s<span class="chip">and many more</span></div><div style="height:80px"></div></div>'%(chips(MFG,' g'),chips(TRD)))
# ABOUT
page('/about/','About Jasuja Hosiery | Hosiery Manufacturer Since 1976','Jasuja Hosiery was established in 1976. We manufacture our own brands, produce OEM for partners and trade in leading hosiery, thermal and apparel brands.',
head('About','Nearly five decades of hosiery.','Jasuja Hosiery was established in 1976. Today we manufacture our own brands, produce as an OEM, and trade in well-known names in hosiery, thermals and cotton apparel.')+'<div class="wrap"><div class="grid">%s%s%s</div>%s<div style="height:80px"></div></div>'%(card('Manufacture','Made in India','Thermal wear and quilts under our own labels.'),card('OEM','Made for you','Private-label manufacturing for partner brands.'),card('Trade','Sourced with care','A wide range of trusted brands under one roof.'),CTA),ld(ORG))
# FAQ
fl=''.join('<details><summary>%s</summary><p>%s</p></details>'%(E(q),E(a)) for q,a in D['faqs'])
page('/faq/','FAQ | Jasuja Hosiery','Answers about Jasuja Hosiery: brands, OEM, wholesale enquiries, contact details, and how to choose and wash JH Thermals (sizes 36 to 90).',
head('FAQ','Questions, answered.')+'<div class="wrap" style="padding-bottom:80px">%s</div>'%fl,
ld({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in D['faqs']]}))
# BLOG
page('/blog/','Blog: Clothing, Thermal & Hosiery Guides | Jasuja Hosiery','Practical guides on thermals, winter layering, innerwear and hosiery care from Jasuja Hosiery.',
head('Blog','Clothing guides and tips.')+'<div class="wrap post" style="padding-bottom:80px"><div class="grid" style="margin-top:0">%s</div></div>'%''.join(card('',p['t'],E(p['desc']),'/blog/%s/'%p['s']) for p in D['posts']))
for p in D['posts']:
    ps=''.join('<p>%s</p>'%E(x) for x in p['p'])
    page('/blog/%s/'%p['s'],p['t']+' | Jasuja Hosiery',p['desc'],
    '<div class="wrap head"><a class="back" href="/blog/">← All articles</a><h1 style="font-size:clamp(32px,5vw,52px);margin:14px 0">%s</h1><p class="eyebrow">%s</p></div><div class="wrap post" style="padding-bottom:80px"><div class="art">%s<p>Explore our <a href="/products/" style="color:var(--gold)">products</a> or <a href="/contact/" style="color:var(--gold)">contact us</a> for help.</p></div></div>'%(E(p['t']),p['d'],ps),
    ld({"@context":"https://schema.org","@type":"BlogPosting","headline":p['t'],"description":p['desc'],"datePublished":p['d'],"dateModified":p['d'],"mainEntityOfPage":U+'/blog/%s/'%p['s'],"author":{"@type":"Organization","name":"Jasuja Hosiery"},"publisher":{"@type":"Organization","name":"Jasuja Hosiery"}}),'article')
# CONTACT
page('/contact/','Contact Jasuja Hosiery | Phone, WhatsApp, Email & Map','Call +91 93585 83300 or +91 87919 07779, WhatsApp or email info@jasujahosiery.com. Find Jasuja Hosiery on Google Maps.',
head('Contact','Let\'s talk.')+'''<div class="wrap"><div class="cols"><div>
<div class="row"><small>Phone</small><a href="tel:%s">+91 93585 83300</a></div><div class="row"><small>Phone</small><a href="tel:%s">+91 87919 07779</a></div><div class="row"><small>Email</small><a href="mailto:%s">%s</a></div>
<div class="btns" style="justify-content:flex-start"><a class="btn" href="https://wa.me/919358583300">WhatsApp us</a><a class="btn o" href="mailto:%s">Send email</a></div></div>
<div><div class="map"><iframe src="%s" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin" title="Jasuja Hosiery on Google Maps"></iframe></div><p style="margin-top:12px"><a href="https://www.google.com/maps/search/?api=1&amp;query=Jasuja+Hosiery" style="color:var(--gold);font-weight:600">Open in Google Maps →</a></p></div></div><div style="height:80px"></div></div>'''%(PH1,PH2,MAIL,MAIL,MAIL,MAP),ld(ORG))
# 404, robots, sitemap
open(os.path.join(R,'404.html'),'w',encoding='utf-8').write('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found | Jasuja Hosiery</title><meta name="robots" content="noindex"><link rel="stylesheet" href="/style.css"></head><body><div class="wrap hero"><h1>404</h1><p class="lead">This page could not be found.</p><div class="btns"><a class="btn" href="/">Back to home</a></div></div></body></html>')
urls=['/']+[h for h,_ in NAV[1:]]+['/blog/%s/'%p['s'] for p in D['posts']]
open(os.path.join(R,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>%s%s</loc><lastmod>2026-10-05</lastmod></url>\n'%(U,u) for u in urls)+'</urlset>\n')
open(os.path.join(R,'robots.txt'),'w').write('User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n'%U)
print('built',len(urls),'pages')
