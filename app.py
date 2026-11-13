"""Pearls of the Past, Oceans of the Future — educational Streamlit app.
Run: python -m streamlit run app.py
All game quantities and marine scenarios are illustrative, not NASA measurements.
"""
import random
from pathlib import Path
from datetime import date
import streamlit as st

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
st.set_page_config(page_title='Pearls of the Past | UAE Ocean Explorer', page_icon='🐚', layout='centered', initial_sidebar_state='collapsed')
st.markdown("""<style>
/* Responsive layout with a consistent high-contrast light palette. */
:root { color-scheme: light; }
html, body, .stApp, [data-testid="stAppViewContainer"] {
  background: #F4FAFB !important;
  color: #143446 !important;
}
[data-testid="stHeader"] { background: #F4FAFB !important; }
.block-container { max-width: 820px !important; padding: 1.0rem 1.15rem 4rem !important; }
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] strong,
[data-testid="stMarkdownContainer"] em,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4 { color: #143446 !important; }
[data-testid="stMarkdownContainer"] a { color: #006F83 !important; }
[data-testid="stCaptionContainer"] p, .stCaption { color: #36586D !important; }
[data-testid="stMetric"] { background: white !important; border: 1px solid #B9DDE5; padding: 0.75rem; border-radius: 15px; }
[data-testid="stMetric"] * { color: #143446 !important; }
.stButton > button, .stDownloadButton > button, .stLinkButton a {
    width: 100% !important; min-height: 50px !important; border-radius: 15px !important;
    background: #077C7C !important; border: 1px solid #066467 !important;
    color: #FFFFFF !important; font-weight: 700 !important; white-space: normal !important;
    line-height: 1.25 !important; box-shadow: 0 3px 9px rgba(5,70,79,.10);
}
.stButton > button *, .stDownloadButton > button *, .stLinkButton a * { color: #FFFFFF !important; }
.stButton > button:hover, .stDownloadButton > button:hover, .stLinkButton a:hover { background: #05636B !important; color: #FFFFFF !important; }
.stButton > button:disabled { background: #D6E8E9 !important; color: #385667 !important; border-color: #B4CBCE !important; }
.stButton > button:disabled * { color: #385667 !important; }
[data-baseweb="select"] > div, [data-baseweb="input"] > div, textarea, input {
    background: #FFFFFF !important; color: #143446 !important; border-radius: 12px !important;
}
[data-baseweb="select"] > div *, [data-baseweb="input"] > div *, [data-testid="stWidgetLabel"] * { color: #143446 !important; }
[data-testid="stExpander"] { background: #FFFFFF !important; border: 1px solid #C7E3E8 !important; border-radius: 15px !important; }
[data-testid="stExpander"] * { color: #143446 !important; }
[data-testid="stAlert"] { border-radius: 14px !important; }
.hero-photo { width: 100%; height: auto; display: block; border-radius: 17px; border: 1px solid #C4DFE5; }
.photo-credit { font-size: .79rem !important; color: #395B6A !important; margin: 4px 0 15px; }
.photo-credit a { color: #006F83 !important; text-decoration: underline; }
.brand-header { background: linear-gradient(125deg,#006977 0%,#108D8A 60%,#24AFA0 100%);
    border-radius: 20px; padding: 18px 18px 15px; margin: 2px 0 18px; }
.brand-header .kicker { font-size: .81rem; letter-spacing: .09rem; text-transform: uppercase;
    font-weight: 700; color: #DDF8F5 !important; margin-bottom: 5px; }
.brand-header .headline { font-size: 1.75rem; font-weight: 800; line-height: 1.15;
    color: #FFFFFF !important; margin: 0 0 6px; }
.brand-header .tagline { color: #E9FFFD !important; font-size: .94rem; margin: 0; }
.stats-grid { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 8px; margin: 15px 0; }
.stats-grid .stat { background: #FFFFFF; border: 1px solid #C6DFE4; border-radius: 13px;
    padding: 12px 6px; text-align: center; min-width: 0; }
.stats-grid .stat-num { color: #086B76 !important; font-size: 1.45rem; font-weight: 800; line-height: 1.2; }
.stats-grid .stat-label { color: #345568 !important; font-size: .74rem; line-height: 1.2; }
@media (max-width: 640px) {
  .block-container { padding: 0.4rem .72rem 4rem !important; }
  .brand-header { padding: 15px; border-radius: 17px; }
  .brand-header .headline { font-size: 1.46rem; }
  [data-testid="stMarkdownContainer"] h1 { font-size: 1.67rem !important; line-height: 1.2 !important; }
  [data-testid="stMarkdownContainer"] h2 { font-size: 1.37rem !important; }
  .stats-grid .stat-num { font-size: 1.24rem; }
  .stats-grid .stat-label { font-size: .68rem; }
  [data-testid="stHorizontalBlock"] { flex-wrap: wrap !important; }
  [data-testid="column"] { flex: 1 1 100% !important; min-width: 100% !important; width: 100% !important; }
  .hero-photo { max-height: none; object-fit: contain; }
}
</style>""", unsafe_allow_html=True)

if 'points' not in st.session_state: st.session_state.points=0
if 'awards' not in st.session_state: st.session_state.awards=set()
if 'quiz_idx' not in st.session_state: st.session_state.quiz_idx=0
if 'quiz_answers' not in st.session_state: st.session_state.quiz_answers={}
if 'diver' not in st.session_state: st.session_state.diver={'air':100,'stamina':100,'pearls':0,'dives':0,'status':'ready'}
if 'captain' not in st.session_state: st.session_state.captain={'day':1,'supplies':75,'safety':80,'trade':0,'history':[]}
if 'clean' not in st.session_state: st.session_state.clean={'plastic':6,'nets':3,'oil':2,'handled':0}
if 'sat_notes' not in st.session_state: st.session_state.sat_notes=[]

def award(key,points):
    if key not in st.session_state.awards:
        st.session_state.awards.add(key);st.session_state.points+=points

PHOTO_DATA = {
    'hero.svg': ('https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Traditional_Dhow.jpg/960px-Traditional_Dhow.jpg', 'Traditional dhow — Mohammad Kittaneh, CC BY-SA 4.0', 'https://commons.wikimedia.org/wiki/File:Traditional_Dhow.jpg', 'Traditional_Dhow.jpg'),
    'dhow.svg': ('https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Traditional_Dhow.jpg/960px-Traditional_Dhow.jpg', 'Traditional dhow — Mohammad Kittaneh, CC BY-SA 4.0', 'https://commons.wikimedia.org/wiki/File:Traditional_Dhow.jpg', 'Traditional_Dhow.jpg'),
    'pearls.svg': ('https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Pearl_Oysters.jpg/960px-Pearl_Oysters.jpg', 'Pearl oysters — Keith Pomakis, CC BY-SA 2.5 (not a UAE location)', 'https://commons.wikimedia.org/wiki/File:Pearl_Oysters.jpg', 'Pearl_Oysters.jpg'),
    'conserve.svg': ('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Hawksbill_sea_turtle.jpg/960px-Hawksbill_sea_turtle.jpg', 'Hawksbill sea turtle — Cmjohns6, public domain (photographed outside UAE)', 'https://commons.wikimedia.org/wiki/File:Hawksbill_sea_turtle.jpg', 'Hawksbill_sea_turtle.jpg'),
    'earth.svg': ('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Hawksbill_sea_turtle.jpg/960px-Hawksbill_sea_turtle.jpg', 'Marine wildlife photograph — Cmjohns6, public domain (not NASA satellite data)', 'https://commons.wikimedia.org/wiki/File:Hawksbill_sea_turtle.jpg', 'Hawksbill_sea_turtle.jpg'),
}

def img(name,caption=None):
    """Display verified real photographs with readable source attribution.
    If an optional locally-downloaded image is present, show it offline.
    """
    import html
    remote, credit, source, filename = PHOTO_DATA.get(name, PHOTO_DATA['hero.svg'])
    local = ASSETS / 'photos' / filename
    if local.exists():
        st.image(str(local), width='stretch')
    else:
        st.markdown(f'<img class="hero-photo" src="{html.escape(remote,quote=True)}" alt="{html.escape(credit,quote=True)}" loading="lazy">',unsafe_allow_html=True)
    st.markdown(f'<div class="photo-credit">📷 <a href="{html.escape(source,quote=True)}" target="_blank">{html.escape(credit)}</a></div>',unsafe_allow_html=True)
    if caption: st.caption(caption)

def header(title,sub,asset=None):
    st.title(title);st.caption(sub)
    if asset: img(asset)

LANG=st.selectbox('🌐 Language / اللغة',['English','العربية'], key='language')
AR=LANG=='العربية'
def tr(en,ar): return ar if AR else en
st.markdown(f"""<div class="brand-header"><div class="kicker">🌊 UAE Ocean Heritage Explorer</div>
<div class="headline">{tr('Pearls of the Past','لآلئ الماضي')}</div>
<p class="tagline">{tr('Explore traditions • Discover oceans • Play and learn','اكتشف التراث والبحار وتعلم باللعب')}</p></div>""", unsafe_allow_html=True)
PAGES=['🏠 Home','📜 Heritage','🛰️ NASA Ocean Explorer','🧠 Knowledge Quiz','🦪 Pearl Diving Game','⛵ Dhow Captain','🐢 Ocean Rescue','🏆 Achievements','📚 Sources & NASA']
if 'page' not in st.session_state or st.session_state.page not in PAGES:
    st.session_state.page=PAGES[0]
page=st.selectbox(tr('📍 Choose a section','📍 اختر القسم'),PAGES,key='page')
st.caption(tr('⭐ Discovery points: ','⭐ نقاط الاستكشاف: ')+str(st.session_state.points))
st.divider()

def stats(items):
    import html
    st.markdown('<div class="stats-grid">'+''.join(
      '<div class="stat"><div class="stat-num">'+html.escape(str(value))+'</div><div class="stat-label">'+html.escape(str(label))+'</div></div>'
      for label,value in items)+'</div>',unsafe_allow_html=True)

def go_to(destination):
    st.session_state.page=destination

HERITAGE=[
('Pearl diving','الغوص على اللؤلؤ','Pearl diving was an important part of maritime livelihoods and trade in coastal UAE communities before the oil era. Teams worked aboard pearling boats, and harvesting natural pearls required skill and endurance.','كان الغوص على اللؤلؤ جزءاً مهماً من سبل العيش والتجارة في المجتمعات الساحلية الإماراتية قبل عصر النفط.','🦪'),
('Dhows and shipbuilding','السفن الشراعية وصناعتها','Traditional wooden sailing vessels were used in regional fishing, pearling and trading. Sea knowledge, navigation and teamwork helped sailors undertake demanding journeys.','استخدمت السفن الخشبية التقليدية في الصيد والغوص والتجارة، واعتمد البحارة على المعرفة البحرية والعمل الجماعي.','⛵'),
('Fishing traditions','تقاليد الصيد','Fishing helped supply coastal communities with food and livelihoods. Nets, hooks and traditional traps were used in different fishing practices.','كان الصيد مصدراً مهماً للغذاء والرزق، واستخدم الصيادون الشباك والخطاطيف والمصائد التقليدية.','🐟'),
('Trade across the Gulf','التجارة عبر الخليج','Coastal merchants and sailors connected the UAE with ports around the Gulf and Indian Ocean, exchanging goods, knowledge and cultural traditions.','ربط التجار والبحارة الإمارات بالموانئ عبر الخليج والمحيط الهندي لتبادل السلع والمعرفة.','🧭'),
('Oceans today','البحار اليوم','Healthy marine habitats matter for biodiversity and coastal life. Monitoring sea temperature, ocean color and coastal conditions can support environmental research and education.','تساعد مراقبة حرارة سطح البحر ولونه والظروف الساحلية في فهم البيئة البحرية وحمايتها.','🌊')]

if page=='🏠 Home':
    img('hero.svg')
    st.title(tr('Pearls of the Past, Oceans of the Future','لآلئ الماضي، بحار المستقبل'))
    st.write(tr('Discover UAE maritime heritage, complete interactive challenges, and explore how NASA satellites observe our changing oceans.','اكتشف التراث البحري الإماراتي وشارك في أنشطة تفاعلية وتعرّف على مراقبة ناسا للمحيطات.'))
    stats([('Explore topics',5),('Mini-games',3),('Your points',st.session_state.points)])
    st.info(tr('NASA challenge alignment: Imagine Our Connected Earth. For a competition submission, add and analyze genuine NASA satellite imagery in the NASA Ocean Explorer section.','تحدي ناسا: تخيّل أرضنا المترابطة. أضف صور أقمار صناعية حقيقية وحلّلها.'))
    st.markdown('**Choose your next adventure:**')
    st.button('📜 Explore UAE sea heritage', key='nav_heritage', on_click=go_to, args=('📜 Heritage',))
    st.button('🛰️ Explore NASA ocean data', key='nav_nasa', on_click=go_to, args=('🛰️ NASA Ocean Explorer',))
    st.button('🧠 Take the knowledge quiz', key='nav_quiz', on_click=go_to, args=('🧠 Knowledge Quiz',))
    st.button('🦪 Play pearl diving', key='nav_pearl', on_click=go_to, args=('🦪 Pearl Diving Game',))
    st.button('⛵ Captain a dhow', key='nav_dhow', on_click=go_to, args=('⛵ Dhow Captain',))
    st.button('🐢 Protect the ocean', key='nav_rescue', on_click=go_to, args=('🐢 Ocean Rescue',))
    st.caption('Real photographs are credited to their original creators. Illustrative game numbers are fictional.')

elif page=='📜 Heritage':
    header(tr('UAE Maritime Heritage','التراث البحري الإماراتي'),tr('Explore the sea-based traditions that shaped coastal life.','اكتشف التقاليد البحرية التي شكّلت الحياة الساحلية.'),'dhow.svg')
    for name,arabic,body,abody,emoji in HERITAGE:
        with st.expander(f'{emoji} {arabic if AR else name}',expanded=name=='Pearl diving'):
            st.write(abody if AR else body)
            if st.button(tr('Mark explored','تم الاستكشاف'),key='heritage'+name):award('heritage_'+name,10);st.success(tr('Exploration recorded!','تم التسجيل!'))
    st.caption('Historical reference: Abu Dhabi Culture – Maritime Life. See Sources & NASA.')

elif page=='🛰️ NASA Ocean Explorer':
    header(tr('NASA Ocean Explorer','مستكشف محيطات ناسا'),tr('Connect Earth observations to marine habitats and coastal communities.','اربط المراقبة الفضائية بالنظم البيئية البحرية.'),'earth.svg')
    st.success('Official 2026 challenge fit: Imagine Our Connected Earth — an interactive audio-visual experience using NASA Earth-observation data.')
    st.markdown('**Step 1 — View real satellite data**')
    st.write('Open NASA Worldview. Zoom to the UAE coast / Arabian Gulf. Compare two dates or layers, such as **Sea Surface Temperature**, **Chlorophyll a**, or **True Color**. Use the layer information to identify the data source.')
    st.link_button('🌍 Open NASA Worldview', 'https://worldview.earthdata.nasa.gov/')
    st.link_button('🛰 NASA Ocean Color', 'https://oceancolor.gsfc.nasa.gov/')
    st.markdown('**Step 2 — Upload screenshots or images that YOU captured from NASA Worldview**')
    f1=st.file_uploader('Observation A — NASA image',type=['png','jpg','jpeg'],key='obs1')
    if f1: st.image(f1,width='stretch')
    f2=st.file_uploader('Observation B — NASA image',type=['png','jpg','jpeg'],key='obs2')
    if f2: st.image(f2,width='stretch')
    st.markdown('**Step 3 — Record your evidence and explanation**')
    layer=st.selectbox('NASA dataset/layer',['Sea Surface Temperature','Chlorophyll a / Ocean color','True-color satellite image','Sea Surface Temperature Anomaly','Other (specify in notes)'])
    dt1=st.date_input('Observation A date',date(2026,7,1),key='dateA')
    dt2=st.date_input('Observation B date',date(2026,10,1),key='dateB')
    observation=st.text_area('What changed between the observations? Describe only what the imagery supports.',placeholder='Example: Coastal water appears different in color; check cloud cover, season and layer legend before drawing conclusions.')
    link=st.text_input('Copy NASA Worldview view URL (optional)',placeholder='https://worldview.earthdata.nasa.gov/...')
    if st.button('Save NASA observation'):
        if not (f1 and f2):st.warning('Upload two NASA Worldview screenshots before saving your comparison.')
        elif not observation.strip():st.warning('Write your evidence-based observation first.')
        else:
            st.session_state.sat_notes.append({'Layer':layer,'Date A':str(dt1),'Date B':str(dt2),'Observation':observation,'NASA URL':link})
            award('nasa_observation',30);st.success('Saved observation and earned 30 discovery points!')
    if st.session_state.sat_notes:
        st.dataframe(st.session_state.sat_notes,width='stretch')
        import csv,io
        buf=io.StringIO();writer=csv.DictWriter(buf,fieldnames=['Layer','Date A','Date B','Observation','NASA URL']);writer.writeheader();writer.writerows(st.session_state.sat_notes)
        st.download_button('⬇ Download observation notes (CSV)',buf.getvalue(),'nasa_observations.csv','text/csv')
    st.info('Important: The app does not automatically download or analyze NASA numerical measurements. Only images you upload and observations you enter are real evidence. Do not claim game values or illustrative images are NASA measurements.')
    st.markdown('**Think like a scientist:** How could changing ocean temperatures influence marine organisms and coastal communities? What additional evidence would you need?')

elif page=='🧠 Knowledge Quiz':
    header(tr('Maritime Knowledge Quiz','اختبار المعرفة البحرية'),'10 questions • Instant feedback • Earn points','pearls.svg')
    QA=[
        ('What was an important traditional UAE sea-based livelihood?',['Pearl diving','Satellite manufacturing','Steelmaking','Aircraft assembly'],0,'Pearl diving supported many coastal livelihoods.'),
        ('What is a dhow?',['A fish species','A traditional sailing vessel','An ocean satellite','A sea measurement'],1,'A dhow is a traditional wooden sailing vessel.'),
        ('What did traditional fishing communities use?',['Nets and hooks','Rocket engines','Wind turbines only','Satellites for every catch'],0,'Traditional fishing used methods including nets and hooks.'),
        ('Which observation can a satellite help scientists study?',['A sailor’s personal memories','Sea surface temperature','A pearl diver’s feelings','The smell of a harbor'],1,'Satellites can measure or estimate sea surface temperature.'),
        ('Why might scientists look at ocean chlorophyll?',['To estimate phytoplankton patterns','To count historic dhows','To test ship engines','To identify ancient pearl prices'],0,'Chlorophyll observations can offer information about phytoplankton distribution.'),
        ('Which source is useful for NASA satellite imagery?',['NASA Worldview','A random social-media post','An unlabelled drawing','An invented score chart'],0,'NASA Worldview displays satellite imagery and geophysical data layers.'),
        ('Which statement best reflects scientific practice?',['One image proves a long-term trend','Compare dates and consider clouds and context','Assume sea color means pollution','Treat simulations as measured data'],1,'Comparisons require context, proper interpretation and evidence.'),
        ('Which activity connects heritage and modern Earth science?',['Studying coastal livelihoods and ocean observations','Ignoring local history','Using only imaginary measurements','Avoiding all source citations'],0,'Combining local history and real ocean data connects culture and science.'),
        ('What can happen when marine habitats are damaged?',['Marine life can be affected','All fish immediately disappear','Sea temperature becomes zero','Satellites stop working'],0,'Habitat damage can impact marine organisms and ecosystems.'),
        ('Which is an appropriate competition citation?',['NASA imagery with date and layer credited','No references','Call all artwork NASA data','Cite only the team’s name'],0,'Cite the source, dataset/layer and observation date of scientific imagery.')]
    idx=st.session_state.quiz_idx
    if idx>=len(QA):
        correct=sum(st.session_state.quiz_answers.get(i)==QA[i][2] for i in range(len(QA)))
        st.success(f'Quiz finished! Your result: {correct}/{len(QA)}')
        if correct>=8:award('quiz_expert',40)
        if st.button('Restart quiz'):
            st.session_state.quiz_idx=0;st.session_state.quiz_answers={};st.rerun()
    else:
        q,choices,answer,ex=QA[idx];st.progress(idx/len(QA));st.subheader(f'Question {idx+1} / {len(QA)}');st.write(q)
        selected=st.session_state.quiz_answers.get(idx)
        for n,opt in enumerate(choices):
            if st.button(opt,key=f'q{idx}_{n}',width='stretch',disabled=selected is not None):
                st.session_state.quiz_answers[idx]=n
                if n==answer:award(f'question_{idx}',5)
                st.rerun()
        if selected is not None:
            (st.success if selected==answer else st.error)('Correct! '+ex if selected==answer else 'Not quite. '+ex)
            if st.button('Next question'):
                st.session_state.quiz_idx+=1;st.rerun()

elif page=='🦪 Pearl Diving Game':
    header(tr('Pearl Diving Adventure','مغامرة الغوص على اللؤلؤ'),'Fictional resource-management game inspired by heritage; NOT diving guidance.','pearls.svg')
    d=st.session_state.diver
    stats([('Air (game units)', d['air']),('Stamina',d['stamina']),('Pearls',d['pearls'])])
    st.progress(max(0,d['air'])/100)
    if d['status']=='finished':st.error('Expedition ended. Rest and plan your next adventure!')
    else:
        if st.button('🦪 Search for oysters'):
            d['air']-=25;d['stamina']-=20;d['dives']+=1
            found=random.choice([0,1,1,2]);d['pearls']+=found
            st.info(f'You found {found} virtual pearl(s). The experience is fictional.')
        if st.button('🛶 Return to boat'):
            d['air']=100;d['stamina']=min(100,d['stamina']+35);st.info('Returned to boat; resources refreshed.')
        if st.button('🏁 End expedition'):d['status']='finished'
    if d['air']<=0 or d['stamina']<=0:d['status']='finished';st.warning('Your diver reached a game resource limit; expedition ends.')
    if d['pearls']>=3:award('pearl_explorer',30);st.success('Pearl Explorer achievement unlocked!')
    if st.button('Restart pearl game'):
        st.session_state.diver={'air':100,'stamina':100,'pearls':0,'dives':0,'status':'ready'};st.rerun()
    st.caption('This is not a safe or realistic model of historical diving; historical divers faced significant risks. Learn from verified museum resources.')

elif page=='⛵ Dhow Captain':
    header(tr('Dhow Captain Challenge','تحدي قبطان السفينة'),'Choose a route and manage supplies. Fictional decisions and game values.','dhow.svg')
    c=st.session_state.captain
    stats([('Voyage day',c['day']),('Supplies',c['supplies']),('Safety',c['safety'])])
    st.caption('Trading points: '+str(c['trade']))
    if c['day']<=5 and c['supplies']>0 and c['safety']>0:
        choice=st.radio('Choose an action',['Sail to next harbor','Wait for safer weather','Trade at a coastal market'],key='voyage_choice')
        if st.button('Confirm decision'):
            outcomes={'Sail to next harbor':(-17,-14,25,'Sailing advances the journey but uses supplies and increases risk.'),'Wait for safer weather':(-8,12,0,'Waiting conserves safety but consumes supplies.'),'Trade at a coastal market':(-12,-5,30,'Trade earns points but also costs supplies.')}
            supply,safety,trade,note=outcomes[choice];c['supplies']=max(0,c['supplies']+supply);c['safety']=max(0,min(100,c['safety']+safety));c['trade']+=trade;c['day']+=1;c['history'].append({'Day':c['day']-1,'Action':choice,'Result':note});st.rerun()
    else:
        success=c['supplies']>0 and c['safety']>0
        if success:award('captain',30);st.success('Voyage completed! Your choices balanced trade and safety.')
        else:st.error('Voyage stopped because your supplies or safety ran out.')
    if c['history']:st.dataframe(c['history'],width='stretch')
    if st.button('Start a new voyage'):
        st.session_state.captain={'day':1,'supplies':75,'safety':80,'trade':0,'history':[]};st.rerun()
    st.caption('Historically inspired decision-making exercise. Not a historical reconstruction or navigation advice.')

elif page=='🐢 Ocean Rescue':
    header(tr('Ocean Rescue Challenge','تحدي حماية البحار'),'Choose a suitable response to illustrative coastal hazards.','conserve.svg')
    c=st.session_state.clean
    st.write('Find a safe response to each problem. These are fictional activities; do not touch hazardous substances in real life.')
    scenarios=[('Plastic litter','plastic',6,'Organize a supervised coastal clean-up and reduce single-use plastic.'),('Discarded fishing nets','nets',3,'Report entangled marine life or abandoned gear to trained authorities.'),('Suspected oil spill','oil',2,'Report the spill to the relevant environmental authorities; do not attempt personal clean-up.')]
    for name,key,original,best in scenarios:
        with st.expander(f'{name} — {c[key]} situations remaining'):
            st.write(best)
            if st.button('Record responsible action',key='clean_'+key,disabled=c[key]==0):
                c[key]-=1;c['handled']+=1;award(f'cleanup_{key}_{c[key]}',3);st.rerun()
    st.metric('Responsible actions completed',c['handled'])
    if all(c[k]==0 for k in ['plastic','nets','oil']):award('ocean_guardian',35);st.success('Ocean Guardian badge earned!')
    if st.button('Restart ocean rescue'):
        st.session_state.clean={'plastic':6,'nets':3,'oil':2,'handled':0};st.rerun()

elif page=='🏆 Achievements':
    header(tr('My Achievements','إنجازاتي'),'Track progress during this browser session. Scores are educational.','pearls.svg')
    st.metric('Total points',st.session_state.points)
    badges=[('Pearl Explorer','pearl_explorer'),('Dhow Navigator','captain'),('Ocean Guardian','ocean_guardian'),('Heritage Expert','quiz_expert'),('NASA Observer','nasa_observation')]
    for name,key in badges:st.write(('🏅 ' if key in st.session_state.awards else '🔒 ')+name)
    st.caption('Progress is held in the current Streamlit session; it may reset when the server or session restarts.')
    if st.button('Reset all progress'):
        for k in ['points','awards','quiz_idx','quiz_answers','diver','captain','clean','sat_notes']:
            if k in st.session_state:del st.session_state[k]
        st.rerun()

elif page=='📚 Sources & NASA':
    header(tr('Sources and NASA Research','المصادر وأبحاث ناسا'),'Learn where the images and research links come from.','earth.svg')
    st.markdown('''### NASA challenge and data
- [2026 NASA Space Apps: Imagine Our Connected Earth](https://www.spaceappschallenge.org/2026/challenges/imagine-our-connected-earth/)
- [NASA Worldview — satellite data layers](https://worldview.earthdata.nasa.gov/)
- [NASA Ocean Color](https://oceancolor.gsfc.nasa.gov/)

### UAE heritage
- [Abu Dhabi Culture — Maritime Life](https://abudhabiculture.ae/en/cultural-heritage/intangible/heritage-register/social-practices/maritime-life)
- [Sharjah Maritime Museum](https://www.sharjahmuseums.ae/en-us/museums/sharjah-maritime-museum)

### Real-photo credits (Google-indexed images from Wikimedia Commons)
- [Traditional Dhow — Mohammad Kittaneh (CC BY-SA 4.0)](https://commons.wikimedia.org/wiki/File:Traditional_Dhow.jpg)
- [Pearl Oysters — Keith Pomakis (CC BY-SA 2.5)](https://commons.wikimedia.org/wiki/File:Pearl_Oysters.jpg)
- [Hawksbill sea turtle — Cmjohns6 (public domain)](https://commons.wikimedia.org/wiki/File:Hawksbill_sea_turtle.jpg)
- These photos illustrate the subject; only the dhow photo is described as a traditional dhow, and the other pictures are **not claimed to have been taken in the UAE**. Do not describe them as NASA satellite observations.

### About this explorer
This prototype is **not affiliated with or endorsed by NASA**. The real photographs come from Wikimedia Commons, with author and license credits below each image; original vector artwork remains in the assets folder as backup. Game scores, resource values and outcomes are fictional. The satellite explorer includes a NASA Worldview research link and accepts explorer-uploaded NASA screenshots; it does **not** bundle or pre-fetch real NASA observations.

**For a NASA-themed competition submission:** (1) select and study the full official challenge; (2) use at least two properly cited, genuine NASA satellite observations; (3) compare Earth-system interactions using evidence, explaining limitations; (4) make the NASA-data storytelling the central feature, rather than only the quiz or cultural history; (5) cite all external data and disclose use of starter code or AI assistance.
''')
    st.download_button('Download explorer summary',data='Pearls of the Past, Oceans of the Future\nExplore UAE maritime heritage alongside NASA ocean observations.\nScientific evidence: use properly cited NASA Worldview observations.\nNote: Game values are fictional. Not affiliated with NASA.\n',file_name='ocean_explorer_summary.txt')
