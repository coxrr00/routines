"""Builds the routines website (coxrr00.github.io/routines): one page per character at /<name>/.
Run it, then commit and push; GitHub Pages serves the repo root. Copy comes from the approved PDFs (Cindy, Daniel) and Linda's locked vid 6 script + vid 7 DM draft."""
import html, pathlib, sys

ROOT = pathlib.Path(__file__).parent
SITE = "https://coxrr00.github.io/routines"

CHARS = {
  "cindy": dict(
    title="Cindy's Full Routine",
    eyebrow="Cindy's full routine &middot; free",
    h1='Everything I did, start to <em>finish</em>',
    sub="The simple day-to-day routine that finally worked for me at 54. No crazy diets, no starving myself. Just a few habits I stuck with for a year.",
    byline="Cindy Hayes &middot; 55 &middot; Dallas, Texas",
    stats=[("164", "lbs when I started"), ("124", "lbs one year later")],
    quote="It's not magic. It's just what finally worked. If I can do it at fifty-five, you can do it.",
    sig="xo, Cindy",
    colors=dict(hero="#3d1f22", hero2="#5a2c2e", accent="#f0a48f", ink="#2e1f1b", brand="#b8473f", paper="#fbf4ef", card="#ffffff", line="#ecd9d0", muted="#86665c"),
    sections=[
      dict(kind="habits", h="My 5 daily habits", lead="I didn't do these all at once. I added one every couple of weeks until it felt normal.", items=[
        ("Protein first, every meal", "Eggs in the morning, chicken or fish at lunch and dinner. I eat the protein before anything else on the plate. It keeps me full way longer.", "Your doctor said 'eat less'? Mm-mm. Eat smarter."),
        ("Rootation gummies with breakfast", "Every morning with my coffee (I follow the label on the jar). They're part of my routine to support healthy blood sugar, and they've helped with my cravings and that afternoon crash. And no pills to swallow, which I love.", None),
        ("A 10-minute walk after meals", "Just around the block. Even in a hundred-and-five-degree Texas summer, I'd go early in the morning or after dinner. Those little walks added up more than anything.", None),
        ("Strength training 3x a week", "Light dumbbells in my living room, 20 to 30 minutes. Squats, lunges, rows, and presses. Building muscle is what changed the shape of my body.", None),
        ("Cut the sugar (slowly)", "I didn't go cold turkey. I swapped one sugary thing at a time. Sweet tea was the hardest one for this Texas girl!", None),
      ]),
      dict(kind="day", h="What a normal day looks like", lead="Copy this, then make it yours.", rows=[
        ("7:00 am", "Big glass of water. Coffee and my Rootation gummies."),
        ("7:30 am", "Protein breakfast: scrambled eggs, berries, half an avocado."),
        ("8:00 am", "10-minute walk around the neighborhood."),
        ("12:30 pm", "Lunch: big salad with grilled chicken. Protein first."),
        ("1:00 pm", "Short walk. This is what beat my after-lunch crash."),
        ("3:30 pm", "Snack if I'm hungry: Greek yogurt or a cheese stick."),
        ("5:30 pm", "Mon / Wed / Fri: 25 minutes of dumbbells in the living room."),
        ("6:30 pm", "Dinner: fish or lean meat and veggies. Tex-Mex night = fajita bowl, no tortilla."),
        ("7:15 pm", "Evening walk with my husband."),
        ("9:00 pm", "Kitchen's closed. Herbal tea if I want something."),
      ]),
      dict(kind="swaps", h="My easy swaps", items=[
        ("Sweet tea", "Unsweet tea with lemon"), ("Late-night chips", "Kitchen closes at 9"),
        ("Kolaches for breakfast", "Eggs and fruit"), ("Soda", "Sparkling water with lime"),
      ]),
    ],
    gummy_h="The gummies in my routine",
    gummy_p="Rootation berberine gummies, berry flavored, with apple cider vinegar, milk thistle and Ceylon cinnamon. They're part of my routine to support healthy blood sugar, and they've helped with my cravings. No pills to swallow.",
    link="https://linktw.in/mchdpv",
    disclaimer="Cindy Hayes is an AI-generated character (#syntheticperformer). This page is for general information and inspiration only and is not medical advice. Never stop any medication on your own. Rootation gummies are a dietary supplement, not a weight loss product, and are not intended to diagnose, treat, cure, or prevent any disease. These statements have not been evaluated by the Food and Drug Administration. My results came from my whole routine over a year. Individual results vary. #rootationpartner #simplert",
  ),
  "daniel": dict(
    title="Daniel's Full Routine",
    eyebrow="Daniel's full routine &middot; free",
    h1='Everything I did, start to <em>finish</em>',
    sub="My grandmother's rules from Busan, back in my own kitchen. No crazy diets, no starving myself. Just a few habits I stuck with for over a year.",
    byline="Daniel Park &middot; 61",
    stats=[("233", "lbs when I started"), ("185", "lbs over a year later")],
    quote="In Korea nobody tells you you're too old. I'm 61 and I feel better than I have in years. If I can do it, you can do it.",
    sig="Daniel",
    colors=dict(hero="#1c2b27", hero2="#2b3f39", accent="#b9d6b0", ink="#1d2522", brand="#3f6b5c", paper="#f2f4f0", card="#ffffff", line="#d9e0da", muted="#5e6e67"),
    sections=[
      dict(kind="habits", h="My 6 daily habits", lead="I didn't do these all at once. I added one every couple of weeks until it felt normal.", items=[
        ("Soup before rice", "A small bowl of soup first, the way my grandmother served every meal. Then the rest of the plate. It slows me down, and I stopped going back for seconds.", "Eat like Grandma, not like the drive-thru."),
        ("Something fermented with every meal", "A little kimchi on the side, doenjang in my soup, or a bowl of plain yogurt. Grandma never put a meal on the table without it, so neither do I.", None),
        ("Barley tea instead of soda", "I keep a jug of cold roasted barley tea in the fridge. No sugar. After 35 years of energy drinks at a desk job, this was the big one.", None),
        ("Rootation gummies with breakfast", "Every morning with breakfast (I follow the label on the jar). They're part of my routine to support healthy blood sugar, and they've helped with my cravings and that afternoon slump. And no pills to swallow.", None),
        ("A 15-minute walk after dinner", "Out the door as soon as the dishes are done. Rain or shine. Those little walks added up more than anything.", None),
        ("Strength class twice a week", "I started light and felt silly. Now it's the best part of my week. Building muscle is what changed the shape of my body.", None),
      ]),
      dict(kind="day", h="What a normal day looks like", lead="Copy this, then make it yours.", rows=[
        ("6:30 am", "Big glass of water, then a cup of warm barley tea."),
        ("7:00 am", "Breakfast: eggs, a little rice and kimchi. Rootation gummies."),
        ("12:30 pm", "Lunch: soup first, then grilled fish or chicken with vegetables."),
        ("1:00 pm", "Short walk around the block. This is what beat my after-lunch slump."),
        ("3:30 pm", "Snack if I'm hungry: plain yogurt or a handful of nuts."),
        ("5:30 pm", "Tue / Thu: strength class."),
        ("6:30 pm", "Dinner: soup first, then lean meat or tofu, vegetables, small bowl of rice."),
        ("7:15 pm", "15-minute walk after dinner."),
        ("9:00 pm", "Kitchen's closed. Warm barley tea if I want something."),
      ]),
      dict(kind="swaps", h="My easy swaps", items=[
        ("Energy drinks", "Cold barley tea"), ("Drive-thru lunch", "Packed lunch, soup first"),
        ("Office snacks", "Plain yogurt or nuts"), ("Soda with dinner", "Sparkling water"),
      ]),
    ],
    gummy_h="The gummies in my routine",
    gummy_p="Rootation berberine gummies, berry flavored, with apple cider vinegar, milk thistle and Ceylon cinnamon. They're part of my routine to support healthy blood sugar, and they've helped with my cravings and that afternoon slump. No pills to swallow.",
    link="https://linktw.in/sccaxx",
    disclaimer="Daniel Park is an AI-generated character (#syntheticperformer). This page is for general information and inspiration only and is not medical advice. Never stop any medication on your own. Rootation gummies are a dietary supplement, not a weight loss product, and are not intended to diagnose, treat, cure, or prevent any disease. These statements have not been evaluated by the Food and Drug Administration. My results came from my whole routine over more than a year. Individual results vary. #rootationpartner #simplert",
  ),
  "linda": dict(
    title="Linda's Daily Routine",
    eyebrow="Linda's routine &middot; free",
    h1='My whole morning and <em>evening</em> routine',
    sub="Nothing fancy. At seventy-four, these are the small things I actually stick to, from the first cup in the morning to lights out.",
    byline="Linda &middot; 74",
    stats=None,
    quote="It's the up and down. Something sweet, a crash an hour later, and you're right back for more. This is how I got off that ride.",
    sig="Linda",
    colors=dict(hero="#1f2433", hero2="#33394d", accent="#e8c98f", ink="#22252e", brand="#566a8f", paper="#f4f2ee", card="#ffffff", line="#e0ddd5", muted="#666b78"),
    sections=[
      dict(kind="recipe", h="Morning: my warm drink", lead="The first thing I changed, and I've stuck with it. I sip it warm every morning before breakfast.", items=[
        ("2 cups", "water, warmed in a small pan"),
        ("1 tbsp", "apple cider vinegar"),
        ("&frac12;", "lemon, juiced"),
        ("1 pinch", "Ceylon cinnamon"),
      ], note="It's simple, it tastes better than you'd think, and it sets the tone for my day. Then my Rootation gummies with breakfast (I follow the label on the jar)."),
      dict(kind="habits", h="Evening: how I wind down", lead="It took a few weeks, but most nights now I sleep right through.", items=[
        ("No coffee after lunch", "Not even half a cup.", None),
        ("The kitchen closes after dinner", "Once the dishes are done, that's it for the day. No more trips to the pantry.", None),
        ("Chamomile, an hour before bed", "A warm cup of chamomile tea. No caffeine.", None),
        ("A cool, dark bedroom", "And my phone stays in the kitchen.", None),
      ]),
    ],
    gummy_h="The gummies I take every day",
    gummy_p="My Rootation berberine gummies, berry flavored, with apple cider vinegar, milk thistle and Ceylon cinnamon. They're made to support healthy blood sugar as part of a routine, and for me they've helped with the late-night cravings. No pills to swallow.",
    link="https://linktw.in/krpurv",
    disclaimer="Linda is an AI-generated character (#syntheticperformer). This page is for general information and inspiration only and is not medical advice. Never stop any medication on your own. Rootation gummies are a dietary supplement and are not intended to diagnose, treat, cure, or prevent any disease. These statements have not been evaluated by the Food and Drug Administration. Individual results vary. #rootationpartner #simplert",
  ),
}

CSS = """
:root{--hero:%(hero)s;--hero2:%(hero2)s;--accent:%(accent)s;--ink:%(ink)s;--brand:%(brand)s;--paper:%(paper)s;--card:%(card)s;--line:%(line)s;--muted:%(muted)s;
--display:"Barlow Condensed","Arial Narrow",sans-serif;--body:"Figtree","Segoe UI",system-ui,sans-serif;--hand:"Caveat","Segoe Script",cursive;color-scheme:light}
/* Layout: dark hero band with a card that overlaps it, then one narrow reading column; sticky shop bar at the bottom */
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.6;margin:0;padding-bottom:calc(84px + env(safe-area-inset-bottom,0px))}
.wrap{max-width:640px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.hero{background:radial-gradient(120%% 90%% at 50%% 0%%,var(--hero2),var(--hero) 70%%);color:#f6f1ea;text-align:center}
.hero .wrap{padding-block:44px 92px}
.eyebrow{font-family:var(--display);font-weight:600;letter-spacing:.18em;text-transform:uppercase;font-size:14px;color:var(--accent)}
h1{font-family:var(--display);font-weight:700;font-size:clamp(40px,10vw,62px);line-height:.98;margin:14px 0 16px;text-wrap:balance;letter-spacing:-.005em}
h1 em{font-style:normal;color:var(--accent)}
.sub{color:#e6ddd3;max-width:30em;margin:0 auto;text-wrap:pretty}
.by{display:inline-flex;align-items:center;gap:12px;margin-top:22px;font-size:15px;color:#d9cfc4}
.by img{width:48px;height:48px;border-radius:50%%;border:2px solid var(--accent);object-fit:cover}
.lift{margin-top:-64px;position:relative}
.intro{background:var(--card);border-radius:14px;box-shadow:0 14px 40px rgba(0,0,0,.12);padding:24px}
.stats{display:flex;align-items:center;justify-content:center;gap:18px;padding-bottom:18px;margin-bottom:18px;border-bottom:1px dashed var(--line)}
.stat{text-align:center}
.stat b{display:block;font-family:var(--display);font-weight:700;font-size:52px;line-height:1;color:var(--brand);font-variant-numeric:tabular-nums}
.stat span{display:block;line-height:1.35;margin-top:4px;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.arrow{font-family:var(--display);font-size:34px;color:var(--line)}
.quote{font-size:18px;font-style:italic;margin:0}
.sig{font-family:var(--hand);font-size:30px;color:var(--brand);margin-top:6px;line-height:1}
section{padding-top:44px}
h2{font-family:var(--display);font-weight:700;font-size:34px;line-height:1.05;margin:0 0 6px;text-wrap:balance}
.lead{color:var(--muted);margin:0 0 20px}
ol.habits{list-style:none;margin:0;padding:0;display:grid;gap:12px;counter-reset:h}
ol.habits li{counter-increment:h;display:grid;grid-template-columns:44px 1fr;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px}
ol.habits li::before{content:counter(h);font-family:var(--display);font-weight:700;font-size:30px;line-height:1;color:var(--brand);text-align:center;padding-top:2px}
ol.habits h3{margin:0 0 4px;font-size:18px;line-height:1.3}
ol.habits p{margin:0;font-size:16px}
ol.habits .say{display:block;margin-top:8px;font-style:italic;color:var(--brand)}
.day{display:grid;gap:0;border-left:2px solid var(--line);margin-left:6px}
.row{display:grid;grid-template-columns:86px 1fr;gap:12px;padding:10px 0 10px 18px;position:relative}
.row::before{content:"";position:absolute;left:-7px;top:17px;width:12px;height:12px;border-radius:50%%;background:var(--paper);border:2px solid var(--brand)}
.row time{font-family:var(--display);font-weight:600;font-size:18px;color:var(--brand);font-variant-numeric:tabular-nums;white-space:nowrap}
.row span{min-width:0}
.swaps{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px}
.swap{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;font-size:16px}
.swap s{color:var(--muted);text-decoration-color:var(--brand)}
.swap b{display:block;font-weight:600}
.recipe{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.ing{display:grid;grid-template-columns:90px 1fr;gap:12px;padding:12px 18px;border-bottom:1px dashed var(--line)}
.ing b{font-family:var(--display);font-weight:700;font-size:22px;color:var(--brand);line-height:1.2}
.recipe p{margin:0;padding:14px 18px;font-size:16px}
.gummy{background:var(--hero);color:#f1ebe3;border-radius:14px;padding:26px 24px;margin-top:44px}
.gummy h2{color:#fff}
.gummy p{margin:0 0 18px;color:#ddd3c8}
.btn{display:inline-block;background:var(--accent);color:var(--hero);font-weight:700;text-decoration:none;padding:14px 22px;border-radius:999px;font-size:17px}
.btn:focus-visible{outline:3px solid #fff;outline-offset:3px}
footer{font-size:12px;line-height:1.55;color:var(--muted);padding-block:32px 24px}
.bar{position:fixed;left:0;right:0;bottom:0;padding:12px max(16px,env(safe-area-inset-right,0px)) calc(12px + env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px));background:rgba(255,255,255,.92);backdrop-filter:blur(8px);border-top:1px solid var(--line);display:flex;justify-content:center}
.bar .btn{background:var(--brand);color:#fff;width:100%%;max-width:420px;text-align:center}
@media (max-width:420px){.row{grid-template-columns:70px 1fr}.stat b{font-size:44px}.intro{padding:20px}}
"""

def section_html(s):
    out = [f'<section><h2>{s["h"]}</h2>']
    if s.get("lead"): out.append(f'<p class="lead">{s["lead"]}</p>')
    k = s["kind"]
    if k == "habits":
        out.append('<ol class="habits">')
        for h, p, say in s["items"]:
            q = f'<span class="say">&ldquo;{html.escape(say)}&rdquo;</span>' if say else ""
            out.append(f'<li><div><h3>{html.escape(h)}</h3><p>{html.escape(p)}{q}</p></div></li>')
        out.append('</ol>')
    elif k == "day":
        out.append('<div class="day">')
        for t, d in s["rows"]:
            out.append(f'<div class="row"><time>{t}</time><span>{html.escape(d)}</span></div>')
        out.append('</div>')
    elif k == "swaps":
        out.append('<div class="swaps">')
        for a, b in s["items"]:
            out.append(f'<div class="swap"><s>{html.escape(a)}</s><b>{html.escape(b)}</b></div>')
        out.append('</div>')
    elif k == "recipe":
        out.append('<div class="recipe">')
        for amt, what in s["items"]:
            out.append(f'<div class="ing"><b>{amt}</b><span>{html.escape(what)}</span></div>')
        out.append(f'<p>{html.escape(s["note"])}</p></div>')
    out.append('</section>')
    return "\n".join(out)

def page(key, c):
    stats = ""
    if c["stats"]:
        (a, al), (b, bl) = c["stats"]
        stats = f'<div class="stats"><div class="stat"><b>{a}</b><span>{al}</span></div><div class="arrow" aria-hidden="true">&rarr;</div><div class="stat"><b>{b}</b><span>{bl}</span></div></div>'
    first = c["byline"].split(" &middot;")[0]
    desc = html.escape(c["sub"].replace("&middot;", "-"), quote=True)
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{c['title']}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{c['title']}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/{key}.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="../{key}.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Caveat:wght@600&family=Figtree:ital,wght@0,400;0,600;0,700;1,400&display=swap">
<style>{CSS % c['colors']}</style>
</head><body>
<header class="hero"><div class="wrap">
<div class="eyebrow">{c['eyebrow']}</div>
<h1>{c['h1']}</h1>
<p class="sub">{c['sub']}</p>
<div class="by"><img src="../{key}.jpg" alt="{first}"><span>{c['byline']}</span></div>
</div></header>
<main class="wrap">
<div class="lift"><div class="intro">{stats}<p class="quote">&ldquo;{html.escape(c['quote'])}&rdquo;</p><div class="sig">{c['sig']}</div></div></div>
{''.join(section_html(s) for s in c['sections'])}
<div class="gummy"><h2>{c['gummy_h']}</h2><p>{html.escape(c['gummy_p'])}</p><a class="btn" href="{c['link']}" target="_blank" rel="noopener">See them on Amazon</a></div>
<footer>{c['disclaimer']}</footer>
</main>
<div class="bar"><a class="btn" href="{c['link']}" target="_blank" rel="noopener">Get the gummies I take</a></div>
</body></html>
"""

for key, c in CHARS.items():
    if "—" in str(c): sys.exit(f"em-dash in {key}")
    (ROOT / key).mkdir(exist_ok=True)
    (ROOT / key / "index.html").write_text(page(key, c), encoding="utf-8")
    print("wrote", key)
