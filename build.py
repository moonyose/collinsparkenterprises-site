import json,os,html
C=json.load(open('img/credits.json'))
src=lambda c:c.get('source','Wikimedia Commons')
EMAIL='austin.munoz@collinsparkenterprises.com'
def credits():
  li=''.join(f'<li>“<a href="{c["page"]}">{html.escape(c["file"])}</a>” by {html.escape(c["artist"])}, licensed <a href="{c["licurl"]}">{c["license"]}</a>, via {src(c)}. Resized and compressed.</li>' for c in C)
  return f'<details class="credits"><summary>Photo credits</summary><ul>{li}</ul><p>Artworks shown: <em>ETERNITY NOW</em> by Sylvie Fleury (The Bass); <em>Miami Mountain</em> by Ugo Rondinone (Collins Park). Photos used under the licenses above; no endorsement by the photographers, artists or The Bass is implied.</p></details>'
def page(path,title,body,hero=False):
  d='' if path=='' else '../'*path.count('/')+'../'
  root=d or './'
  head=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="Collins Park Enterprises LLC, a Florida company that builds mobile apps."><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Josefin+Sans:wght@300;400;600&family=Lato:wght@300;400;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="{root}style.css"></head><body>
<header class="nav{' over' if hero else ''}"><a class="brand" href="{root}">Collins Park Enterprises</a><nav><a href="{root}#apps">Apps</a><a href="{root}#contact">Contact</a><a href="{root}terms/">Terms</a></nav></header>'''
  foot=f'''<footer><div class="wrap"><p>© 2026 Collins Park Enterprises LLC · Miami Beach, Florida · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p><a href="{root}privacy/lanesync/">LaneSync privacy</a> · <a href="{root}privacy/stridelab/">StrideLab privacy</a> · <a href="{root}privacy/trolley-tracker/">Trolley Tracker privacy</a> · <a href="{root}terms/">Terms</a></p>{credits()}</div></footer></body></html>'''
  out=os.path.join(path,'index.html') if path else 'index.html'
  if path: os.makedirs(path,exist_ok=True)
  open(out,'w').write(head+body.replace('{root}',root)+foot)

page('','Collins Park Enterprises LLC',f'''
<section class="hero"><img class="hero-img" src="img/hero-eternity-now.jpg" alt="The Bass museum facade in Miami Beach with Sylvie Fleury's ETERNITY NOW sign under a blue sky"><div class="hero-shade"></div>
<div class="wrap hero-text"><p class="kicker">Miami Beach · Florida</p><h1>Thoughtful apps,<br><em>made by the sea</em></h1><p class="sub">Collins Park Enterprises builds small, beautifully focused mobile apps from a corner of Miami Beach between the museum and the sea.</p><a class="btn light" href="#apps">Discover our apps</a></div></section>
<div class="deco"><span></span><i>◆</i><span></span></div>
<main>
<section class="wrap split"><div><p class="kicker">About us</p><h2>Built in Collins Park</h2><p>Collins Park Enterprises LLC is a Florida limited liability company that designs and develops mobile apps for iPhone, Apple Watch and Android. Our apps do one job well, keep your data on your device wherever possible, and never show ads.</p><p>Home base is the Collins Park neighborhood, steps from The Bass and Ugo Rondinone's <em>Miami Mountain</em>.</p></div>
<figure class="photo tilt"><img src="img/miami-mountain.jpg" alt="Miami Mountain, Ugo Rondinone's stack of brightly painted boulders, in Collins Park"></figure></section>
<section id="apps" class="apps"><div class="wrap"><p class="kicker">Our apps</p><h2>Three apps, made with care</h2><p class="intro">Each one does a single job beautifully, keeps your data on your device, and never shows ads.</p><div class="cards">
<article class="card c1"><img src="img/icons/lanesync.png" alt="LaneSync icon" width="88" height="88"><h3>LaneSync</h3><p>A sprint timer. Two phones, or a phone and an Apple Watch, time runners from the start signal to the finish line, with automatic finish detection.</p><a href="privacy/lanesync/">Privacy policy</a></article>
<article class="card c2"><img src="img/icons/stridelab.png" alt="StrideLab icon" width="88" height="88"><h3>StrideLab</h3><p>Sprint video analysis. Record or import a sprint and get a pose-skeleton overlay, measurements and coaching tips. StrideLab Pro subscriptions are optional.</p><a href="privacy/stridelab/">Privacy policy</a></article>
<article class="card c3"><img src="img/icons/trolley-tracker.png" alt="Trolley Tracker icon" width="88" height="88"><h3>Trolley Tracker</h3><p>The Miami Beach trolley in real time, with arrival countdowns for nearby stops and the city water taxi schedule.</p><a href="privacy/trolley-tracker/">Privacy policy</a></article>
</div></div></section>
<section class="wrap gallery"><figure class="photo"><img src="img/bass-lawn.jpg" alt="Palm-lined lawn of Collins Park leading to The Bass museum"></figure><figure class="photo"><img src="img/miami-mountain-2.jpg" alt="Miami Mountain sculpture against a blue sky with palm trees"></figure></section>
<section id="contact" class="wrap contact"><div class="contact-card"><p class="kicker">Say hello</p><h2>Contact</h2><p class="big"><a href="mailto:{EMAIL}">{EMAIL}</a></p><p>We read every message and reply by email, usually within two business days.</p></div></section>
</main>''',hero=True)

def policy(slug,name,eff,sections):
  body=f'<main class="wrap doc"><h1>{name} Privacy Policy</h1><p class="muted">Effective {eff}</p>'+sections+f'''
<h2>Who we are and how to contact us</h2><p>{name} is published by Collins Park Enterprises LLC, a Florida limited liability company ("we", "us"). The best way to reach us is by email. Questions about this policy or your data: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Your rights</h2><p>Depending on where you live (for example under the GDPR or U.S. state privacy laws), you may have rights to access, correct, delete or object to the processing of personal data about you. Because the app keeps your data on your device, you can exercise most of these directly in the app. For anything else, email us and we will respond within the time required by law.</p>
<h2>Children</h2><p>{name} is not directed to children under 13, and we do not knowingly collect personal information from children.</p>
<h2>Security</h2><p>Data stays in the app's storage on your device and is protected by your device's own security. No method of storage or transmission is completely secure, but we do not hold a copy of your data.</p>
<h2>Changes</h2><p>If the app's handling of information changes, we will update this page and its effective date before the change ships in an app update.</p></main>'''
  page(f'privacy/{slug}',f'{name} Privacy Policy · Collins Park Enterprises',body)

policy('lanesync','LaneSync','October 18, 2026','''
<p class="lead"><strong>In short:</strong> LaneSync has no accounts, no servers, no analytics, no advertising and no third-party tracking. Times, runner names, notes and video clips stay on your own devices. We do not collect, receive, sell or share your data.</p>
<h2>What LaneSync stores, on your device</h2><ul>
<li><strong>Results:</strong> date, distance, time, pace, clock-sync figures and the runner names and notes you enter. Kept until you delete them or the app.</li>
<li><strong>Roster:</strong> runner names and groups you type in.</li>
<li><strong>Finish-line video</strong> recorded by the finish phone during a session, and short clips cut from it. Working footage is deleted as the session goes on, or when you save or discard the session. A clip is kept longer only if you save it to Photos.</li>
<li><strong>Settings</strong> such as distance unit and finish chime.</li>
<li><strong>Subscription status</strong> (which LaneSync Pro plan is active and when it ends) and a free-workout counter, kept on the device (the counter also in the device keychain, never synced).</li></ul>
<p>Ordinary app data may be included in your own device backups, which are handled by Apple or Google under their policies. We cannot access them.</p>
<h2>Permissions and why</h2><ul>
<li><strong>Camera</strong> (finish phone): films the finish line to detect runners crossing it. Detection uses on-device body-pose analysis, which looks for body positions, not faces or identities. No audio is recorded.</li>
<li><strong>Local network / nearby devices:</strong> the start and finish phones connect directly to each other over Bluetooth and peer-to-peer Wi-Fi to sync clocks and hand over times and clips. This never goes through the internet or through us.</li>
<li><strong>Add to Photos</strong> (optional): only when you choose to save a finish clip.</li>
<li><strong>Health / workout session</strong> (watch): starts a workout session so the watch timer keeps running during the countdown. LaneSync reads no health data and saves no workout.</li></ul>
<p>You can change these permissions at any time in your device settings.</p>
<h2>Data that moves between devices</h2><p>Only directly between nearby devices you are timing with: clock-sync messages, start and finish times, clips and saved results, plus a yes/no flag for whether the start phone has LaneSync Pro, used for that session only. Each device is shown to the other by its device name.</p>
<h2>Sharing</h2><p>Exports (CSV, text, result-card images) leave the app only when you share them through the system share sheet, and are then governed by the service you send them to.</p>
<h2>What we do not do</h2><ul><li>No account, sign-in, email or phone number is requested.</li><li>No analytics, crash-reporting, advertising or tracking software, and no third-party SDKs.</li><li>No connection to any server operated by us. No location data is used. No data is sold or used for advertising.</li></ul>
<h2>Purchases</h2><p>LaneSync Pro is an auto-renewing subscription sold by the app store (Apple App Store or Google Play). The store processes payment; we never receive your name, account or payment details. The app receives only the store's confirmation of which plan is active and when it renews or ends.</p>
<h2>Diagnostics from the platform</h2><p>If you have chosen in your device settings to share analytics with app developers, Apple or Google may give us anonymized crash reports and usage statistics. That sharing is controlled by you in your device settings.</p>
<h2>Deleting your data</h2><p>Delete results, runners and sessions in the app, or delete the app to remove everything it stored (except the free-workout counter in the device keychain). Copies you exported or saved to Photos are separate.</p>''')

policy('stridelab','StrideLab','October 18, 2026','''
<p class="lead"><strong>In short:</strong> StrideLab does not collect any data. Your videos, their analyses and your settings stay on your device. There are no accounts, ads, analytics or tracking, and nothing is sent to us.</p>
<h2>What we collect</h2><p>Nothing. StrideLab has no server and no accounts. It does not send your videos, analyses, settings or any information about you or your device to us or anyone else. It contains no advertising, analytics, crash-reporting or tracking software, and does not use the advertising identifier.</p>
<h2>What stays on your device</h2><ul>
<li><strong>Videos</strong> you record in StrideLab or import from Photos, kept in StrideLab's own storage.</li>
<li><strong>Analyses:</strong> the body positions (a pose skeleton of joint points) measured from your videos, the measurements and coaching tips. These are computed on your device and saved next to the video.</li>
<li><strong>Corrections and settings</strong> you make, such as marked steps, moved joints, camera and coaching preferences.</li>
<li><strong>Subscription status:</strong> a copy of your StrideLab Pro entitlement in the device keychain so Pro works offline. Not synced.</li></ul>
<p>Videos and analyses are excluded from cloud backup because of their size. Settings and the clip list may be included in your device's own backup.</p>
<h2>Camera</h2><p>Used to record sprints in the app. Video only, never sound; recordings stay on your device.</p>
<h2>Photos</h2><p><strong>Importing:</strong> you choose videos with the system photo picker, which gives StrideLab only the videos you pick. If you allow photo library read access, StrideLab uses it only to look up details of the video you picked (when it was filmed, whether it is slow-motion) and to copy a slow-motion original. If you decline, importing still works.<br><strong>Saving:</strong> if "Also save to camera roll" is on, recordings are also saved to Photos; "Save video with skeleton" saves that video to Photos. Both need add-to-Photos permission.</p>
<h2>Purchases</h2><p>StrideLab Pro subscriptions are sold and processed by the app store. We never see your payment details, name or store account. The app checks your subscription with the store on your device; no StrideLab server is involved. Cancel any time in your store account's subscription settings.</p>
<h2>Sharing</h2><p>Videos, frames and scorecards leave your device only when you share or save them yourself.</p>
<h2>Deleting your data</h2><p>Delete a clip to remove its video, analysis and corrections. Deleting the app removes everything StrideLab stored. Copies in Photos or shared elsewhere are not affected.</p>''')

policy('trolley-tracker','Trolley Tracker','October 18, 2026','''
<p class="lead"><strong>In short:</strong> Trolley Tracker has no accounts and no advertising. Your location is used only on your device to sort nearby stops and is never sent to us. We receive information only if you choose to send feedback.</p>
<h2>Location</h2><p>If you allow location access while using the app, your location is used only on your device to show where you are on the map and to sort trolley stops by distance. It is not sent to us, not stored by us, and not included in feedback. The app works without location; you can search stops by street or stop number instead.</p>
<h2>Saved stops and settings</h2><p>Stops you save, arrival-alert preferences and app settings are stored on your device and are never sent to us.</p>
<h2>Notifications</h2><p>If you ask to be alerted when a trolley is a few minutes away, the app schedules a notification on your device. We do not use push-notification servers for this.</p>
<h2>Trolley and map data</h2><p>The app downloads public trolley positions and arrival predictions from the City of Miami Beach's transit data provider, and displays maps and traffic information using the platform's map service (Apple Maps on iPhone). These requests contain no account or personal information from you, although, as with any internet request, the provider receives your device's IP address. Their handling of that information is governed by their own privacy policies.</p>
<h2>Feedback you choose to send</h2><p>If you use Send feedback, the topic and message you write, and optionally a stop and a reply email address you enter, are submitted to a Google Form that we operate, and stored in Google's services. Unless you switch it off in the form, basic device details (app version, operating system version, device model and data source) are attached to help us fix problems. Your location and saved stops are never included. We use feedback only to respond to you and improve the app, and delete it when it is no longer needed. Google's handling is covered by Google's privacy policy.</p>
<h2>What we do not do</h2><ul><li>No accounts or sign-in.</li><li>No advertising and no tracking across other companies' apps or websites.</li><li>No data is sold.</li></ul>
<h2>Diagnostics from the platform</h2><p>If you have chosen in your device settings to share analytics with app developers, Apple or Google may give us anonymized crash reports and usage statistics.</p>
<h2>Deleting your data</h2><p>Remove saved stops in the app or delete the app to remove everything stored on your device. To have feedback you sent deleted, email us.</p>''')

page('terms','Terms of Use · Collins Park Enterprises',f'''<main class="wrap doc"><h1>Terms of Use</h1><p class="muted">Effective October 18, 2026</p>
<p>These terms apply to the apps published by Collins Park Enterprises LLC ("we", "us"), including LaneSync, StrideLab and Trolley Tracker, and to this website. By using an app you agree to these terms. If you got the app from the Apple App Store, Apple's Licensed Application End User License Agreement (<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">standard EULA</a>) also applies; if these terms conflict with it, the standard EULA controls for that app.</p>
<h2>License</h2><p>We grant you a personal, non-exclusive, non-transferable license to use the apps on devices you own or control, under the rules of the store you got them from. You may not copy, modify, reverse engineer or resell the apps except as the law allows.</p>
<h2>Subscriptions</h2><p>Some apps offer auto-renewing subscriptions (for example LaneSync Pro and StrideLab Pro). Payment is charged to your store account at confirmation of purchase. A subscription renews automatically unless cancelled at least 24 hours before the end of the current period, and your account is charged for renewal within 24 hours before the period ends. Any unused part of a free trial is forfeited when you buy a subscription. You can manage and cancel subscriptions in your store account settings. Refunds are handled by the store under its policies.</p>
<h2>Use at your own risk</h2><p>Times, measurements, coaching tips and arrival predictions are estimates. LaneSync and StrideLab are training aids, not official timing or medical advice; consult a qualified coach or professional before changing your training. Trolley Tracker arrival times depend on third-party data and may be wrong or unavailable; do not rely on them where being late would cause harm. Exercise safely and be aware of traffic and your surroundings.</p>
<h2>Your content</h2><p>Videos, names and other content you create stay yours and, as described in each app's privacy policy, stay on your devices. Make sure you have permission to record and store the people you film, including the consent of a parent or guardian for minors where required.</p>
<h2>Disclaimer and limitation of liability</h2><p>The apps are provided "as is" and "as available", without warranties of any kind, to the extent permitted by law. To the extent permitted by law, we are not liable for indirect, incidental, special or consequential damages, or for loss of data, and our total liability is limited to the amount you paid for the app or subscription in the 12 months before the claim.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of the State of Florida, United States, without regard to conflict-of-laws rules, except where your local consumer law gives you rights that cannot be waived.</p>
<h2>Changes and contact</h2><p>We may update these terms and will post the new version here with a new effective date. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>. We handle all inquiries by email.</p></main>''')
