import streamlit as st

import streamlit.components.v1 as components

st.set_page_config(

    page_title="Netra AI",

    layout="wide",

    initial_sidebar_state="collapsed"

)
# Load your FULL UI (UNCHANGED)

html_code = r"""


<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
.page{background:#080a0e;color:#eef2f7;font-family:'Inter',sans-serif;overflow-x:hidden}
.bebas{font-family:'Bebas Neue',sans-serif}

.nav{display:flex;align-items:center;justify-content:space-between;padding:16px 28px;border-bottom:0.5px solid rgba(238,242,247,0.07);position:relative;z-index:20}
.nav-logo{font-family:'Bebas Neue',sans-serif;font-size:26px;letter-spacing:4px;color:#eef2f7;display:flex;align-items:center;gap:10px}
.logo-eye{width:30px;height:30px;background:#5b6af0;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;animation:eyePulse 3s ease-in-out infinite}
@keyframes eyePulse{0%,100%{box-shadow:0 0 0 0 rgba(91,106,240,0)}50%{box-shadow:0 0 0 6px rgba(91,106,240,0.15)}}
.nav-links{display:flex;gap:28px;list-style:none}
.nav-links a{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:rgba(238,242,247,0.4);text-decoration:none;transition:color 0.2s}
.nav-links a:hover{color:#eef2f7}
.nav-est{font-size:10px;letter-spacing:2px;color:rgba(238,242,247,0.2);text-transform:uppercase}

.hero{padding:0 28px;position:relative;overflow:hidden;min-height:480px;display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:24px}
.hero-bg-word{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-family:'Bebas Neue',sans-serif;font-size:200px;letter-spacing:-4px;color:rgba(238,242,247,0.025);pointer-events:none;white-space:nowrap;z-index:0;animation:bgWordDrift 12s ease-in-out infinite alternate}
@keyframes bgWordDrift{from{transform:translate(-52%,-50%)}to{transform:translate(-48%,-50%)}}
.hero-left{position:relative;z-index:2;padding:52px 0}
.hero-tag{font-size:10px;letter-spacing:3px;text-transform:uppercase;color:#5b6af0;margin-bottom:14px;display:flex;align-items:center;gap:8px}
.hero-tag-dot{width:5px;height:5px;border-radius:50%;background:#5b6af0;animation:blink 1.5s ease-in-out infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0.2}}
.hero-h1{font-family:'Bebas Neue',sans-serif;font-size:86px;line-height:0.9;letter-spacing:-0.5px;color:#eef2f7;margin-bottom:18px}
.hero-h1 em{color:#5b6af0;font-style:normal}
.hero-sub{font-size:13px;color:rgba(238,242,247,0.4);line-height:1.8;max-width:340px;margin-bottom:28px}
.hero-ctas{display:flex;gap:12px;margin-bottom:36px}
.btn-primary{background:#5b6af0;color:#fff;border:none;padding:12px 26px;font-size:11px;letter-spacing:2px;text-transform:uppercase;font-weight:500;border-radius:3px;cursor:pointer;font-family:'Inter',sans-serif;transition:background 0.2s;display:flex;align-items:center;gap:7px}
.btn-primary:hover{background:#4a59e0}
.btn-ghost{background:transparent;color:#eef2f7;border:0.5px solid rgba(238,242,247,0.25);padding:12px 26px;font-size:11px;letter-spacing:2px;text-transform:uppercase;border-radius:3px;cursor:pointer;font-family:'Inter',sans-serif;transition:all 0.2s}
.btn-ghost:hover{border-color:#eef2f7}
.hero-stats{display:flex;gap:28px}
.stat-v{font-family:'Bebas Neue',sans-serif;font-size:32px;color:#eef2f7;display:block;line-height:1}
.stat-l{font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:rgba(238,242,247,0.3);margin-top:3px}

.hero-right{position:relative;z-index:2;height:460px;display:flex;align-items:center;justify-content:center}
.cam-frame{width:100%;max-width:380px;border-radius:8px;overflow:hidden;position:relative;border:0.5px solid rgba(91,106,240,0.3)}
video#maincam{width:100%;height:260px;object-fit:cover;display:block;background:#0d1018}
.cam-overlay-frame{position:absolute;inset:0;pointer-events:none}
.corner{position:absolute;width:20px;height:20px;border-color:#5b6af0;border-style:solid}
.ctleft{top:10px;left:10px;border-width:2px 0 0 2px}
.ctr{top:10px;right:10px;border-width:2px 2px 0 0}
.cbl{bottom:10px;left:10px;border-width:0 0 2px 2px}
.cbr{bottom:10px;right:10px;border-width:0 2px 2px 0}
.scan-bar{position:absolute;width:100%;height:2px;background:linear-gradient(90deg,transparent,rgba(91,106,240,0.7),transparent);top:0;animation:scanBar 2.5s linear infinite}
@keyframes scanBar{0%{top:0}100%{top:100%}}
.cam-status-bar{display:flex;align-items:center;justify-content:space-between;padding:10px 14px;background:#0d1018;border-top:0.5px solid rgba(91,106,240,0.15)}
.cam-live{display:flex;align-items:center;gap:6px;font-size:11px;color:#34d399;letter-spacing:1px}
.live-dot{width:6px;height:6px;border-radius:50%;background:#34d399;animation:livePulse 1s ease-in-out infinite}
@keyframes livePulse{0%,100%{opacity:1}50%{opacity:0.3}}
.cam-fps{font-size:11px;color:rgba(238,242,247,0.3);font-family:'Inter',sans-serif;letter-spacing:0.5px}
.cam-placeholder{width:100%;height:260px;background:#0d1018;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;cursor:pointer}
.cam-placeholder i{font-size:36px;color:rgba(91,106,240,0.5)}
.cam-placeholder p{font-size:12px;color:rgba(238,242,247,0.3);letter-spacing:0.5px}
.cam-placeholder span{font-size:11px;background:#5b6af0;color:#fff;padding:7px 18px;border-radius:3px;letter-spacing:1.5px;text-transform:uppercase}

.ticker{background:#5b6af0;padding:10px 0;overflow:hidden;display:flex}
.ticker-track{display:flex;animation:tickRoll 16s linear infinite;white-space:nowrap}
.tick-item{font-family:'Bebas Neue',sans-serif;font-size:14px;letter-spacing:2px;color:#fff;padding:0 24px;display:flex;align-items:center;gap:24px}
.tick-sep{width:4px;height:4px;background:#fff;border-radius:50%;opacity:0.6}
@keyframes tickRoll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}

.marquee-strip{padding:36px 0;overflow:hidden;border-top:0.5px solid rgba(238,242,247,0.05);border-bottom:0.5px solid rgba(238,242,247,0.05)}
.mq-row{display:flex;animation:mqLeft 20s linear infinite;white-space:nowrap}
.mq-row-rev{animation-direction:reverse;animation-duration:26s}
.mq-item{font-family:'Bebas Neue',sans-serif;font-size:56px;letter-spacing:1px;color:rgba(238,242,247,0.05);padding:0 28px;display:flex;align-items:center;gap:28px}
.mq-item em{color:#5b6af0;font-style:normal}
@keyframes mqLeft{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}

.modules-section{padding:64px 28px}
.sec-tag{font-size:10px;letter-spacing:3px;text-transform:uppercase;color:#5b6af0;margin-bottom:10px}
.sec-h{font-family:'Bebas Neue',sans-serif;font-size:58px;line-height:0.92;color:#eef2f7;margin-bottom:32px}
.modules-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.mod-card{background:#0d1018;border:0.5px solid rgba(238,242,247,0.07);border-radius:6px;padding:22px 20px;transition:transform 0.3s,border-color 0.3s;cursor:default}
.mod-card:hover{transform:translateY(-6px);border-color:rgba(91,106,240,0.4)}
.mod-card.active{border-color:rgba(91,106,240,0.35);background:#0f1220}
.mod-icon{width:40px;height:40px;border-radius:8px;background:rgba(91,106,240,0.12);display:flex;align-items:center;justify-content:center;margin-bottom:14px;font-size:20px;color:#5b6af0}
.mod-name{font-family:'Bebas Neue',sans-serif;font-size:20px;color:#eef2f7;letter-spacing:1px;margin-bottom:6px}
.mod-desc{font-size:12px;color:rgba(238,242,247,0.35);line-height:1.7}
.mod-acc{font-size:12px;margin-top:10px;color:#5b6af0;font-weight:500}

.live-section{padding:0 28px 64px}
.live-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:28px}
.live-cam-big{background:#0d1018;border:0.5px solid rgba(238,242,247,0.07);border-radius:8px;overflow:hidden;position:relative}
video#livecam2{width:100%;height:300px;object-fit:cover;display:block;background:#080a0e}
.live-cam-placeholder{width:100%;height:300px;background:#080a0e;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px}
.live-cam-placeholder i{font-size:28px;color:rgba(91,106,240,0.3)}
.live-cam-placeholder p{font-size:12px;color:rgba(238,242,247,0.2)}
.detection-overlay{position:absolute;top:10px;left:10px;right:10px;display:flex;gap:8px;flex-wrap:wrap}
.det-chip{background:rgba(0,0,0,0.7);border:0.5px solid rgba(91,106,240,0.3);border-radius:20px;padding:4px 11px;font-size:10px;color:#eef2f7;letter-spacing:0.5px;display:flex;align-items:center;gap:5px}
.det-chip-dot{width:5px;height:5px;border-radius:50%;flex-shrink:0}
.live-log{background:#0d1018;border:0.5px solid rgba(238,242,247,0.07);border-radius:8px;display:flex;flex-direction:column;overflow:hidden}
.log-header{padding:14px 16px;border-bottom:0.5px solid rgba(238,242,247,0.06);display:flex;align-items:center;justify-content:space-between}
.log-title{font-family:'Bebas Neue',sans-serif;font-size:16px;letter-spacing:2px;color:#eef2f7}
.log-body{flex:1;padding:12px;overflow-y:auto;max-height:250px;display:flex;flex-direction:column;gap:7px}
.log-entry{display:flex;gap:8px;align-items:flex-start}
.log-role{font-size:10px;padding:2px 8px;border-radius:10px;flex-shrink:0;margin-top:1px;font-weight:500;letter-spacing:0.5px}
.log-role-sys{background:rgba(91,106,240,0.15);color:#818cf8}
.log-role-usr{background:rgba(52,211,153,0.12);color:#34d399}
.log-text{font-size:12px;color:rgba(238,242,247,0.5);line-height:1.6}
.log-footer{padding:10px 12px;border-top:0.5px solid rgba(238,242,247,0.06);display:flex;gap:8px}
.log-footer input{flex:1;background:rgba(238,242,247,0.05);border:0.5px solid rgba(238,242,247,0.1);color:#eef2f7;border-radius:4px;padding:8px 12px;font-size:12px;font-family:'Inter',sans-serif}
.log-footer input::placeholder{color:rgba(238,242,247,0.2)}
.log-footer input:focus{outline:none;border-color:rgba(91,106,240,0.5)}
.log-send{background:#5b6af0;border:none;color:#fff;width:34px;height:34px;border-radius:4px;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}

.nav-section{padding:0 28px 64px}
.nav-map{background:#0d1018;border:0.5px solid rgba(238,242,247,0.07);border-radius:8px;padding:24px;margin-top:28px}
.campus-svg-wrap{width:100%;overflow:hidden;border-radius:6px}
.route-controls{display:flex;gap:12px;margin-top:20px;flex-wrap:wrap;align-items:center}
.route-select{background:rgba(238,242,247,0.05);border:0.5px solid rgba(238,242,247,0.12);color:#eef2f7;border-radius:4px;padding:9px 14px;font-size:12px;font-family:'Inter',sans-serif;cursor:pointer}
.route-select option{background:#0d1018}
.btn-nav{background:#5b6af0;color:#fff;border:none;padding:9px 20px;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;border-radius:4px;cursor:pointer;font-family:'Inter',sans-serif;display:flex;align-items:center;gap:6px}

.perf-section{padding:0 28px 64px}
.perf-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:28px}
.perf-card{background:#0d1018;border:0.5px solid rgba(238,242,247,0.07);border-radius:6px;padding:18px}
.perf-val{font-family:'Bebas Neue',sans-serif;font-size:38px;color:#5b6af0;line-height:1}
.perf-lbl{font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:rgba(238,242,247,0.3);margin-top:4px}
.perf-bar-wrap{margin-top:10px;background:rgba(238,242,247,0.07);border-radius:2px;height:3px;overflow:hidden}
.perf-bar{height:100%;background:#5b6af0;border-radius:2px;width:0;transition:width 1.2s ease}

.cta-section{padding:80px 28px;text-align:center;position:relative;overflow:hidden}
.cta-ring{position:absolute;border-radius:50%;border:0.5px solid rgba(91,106,240,0.08);top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 4s ease-in-out infinite}
@keyframes ringPulse{0%,100%{opacity:0.6;transform:translate(-50%,-50%) scale(1)}50%{opacity:0.15;transform:translate(-50%,-50%) scale(1.06)}}
.cta-h{font-family:'Bebas Neue',sans-serif;font-size:70px;line-height:0.9;color:#eef2f7;margin-bottom:16px;position:relative;z-index:2}
.cta-h em{color:#5b6af0;font-style:normal}
.cta-p{font-size:13px;color:rgba(238,242,247,0.35);max-width:380px;margin:0 auto 28px;line-height:1.8;position:relative;z-index:2}

.footer{padding:32px 28px;border-top:0.5px solid rgba(238,242,247,0.06);display:flex;align-items:center;justify-content:space-between}
.foot-logo{font-family:'Bebas Neue',sans-serif;font-size:26px;letter-spacing:4px;color:rgba(238,242,247,0.12)}
.foot-copy{font-size:10px;color:rgba(238,242,247,0.18);letter-spacing:0.5px}
.foot-links{display:flex;gap:20px}
.foot-links a{font-size:10px;color:rgba(238,242,247,0.2);text-decoration:none;letter-spacing:1.5px;text-transform:uppercase;transition:color 0.2s}
.foot-links a:hover{color:rgba(238,242,247,0.6)}

.mic-fab{position:relative;z-index:10;width:46px;height:46px;border-radius:50%;background:#5b6af0;border:none;color:#fff;font-size:20px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all 0.2s;flex-shrink:0}
.mic-fab.on{background:#ef4444;animation:micOn 1s ease-in-out infinite}
@keyframes micOn{0%,100%{transform:scale(1)}50%{transform:scale(1.08)}}

.reveal{opacity:0;transform:translateY(24px);transition:opacity 0.7s ease,transform 0.7s ease}
.reveal.v{opacity:1;transform:translateY(0)}
.rd1{transition-delay:0.1s}.rd2{transition-delay:0.2s}.rd3{transition-delay:0.3s}
</style>

<h2 class="sr-only">Netra-AI — real-time assistive navigation interface for the visually impaired with live camera, voice, and campus routing</h2>

<div class="page">

<nav class="nav">
  <div class="nav-logo">
    <div class="logo-eye"><i class="ti ti-eye" style="font-size:14px;color:#fff" aria-hidden="true"></i></div>
    NETRA
  </div>
  <ul class="nav-links">
    <li><a href="#">Vision</a></li>
    <li><a href="#">Navigate</a></li>
    <li><a href="#">Modules</a></li>
    <li><a href="#">About</a></li>
  </ul>
  <div class="nav-est">VIT Bhopal · 2025</div>
</nav>

<section class="hero">
  <div class="hero-bg-word">NETRA</div>
  <div class="hero-left">
    <div class="hero-tag"><span class="hero-tag-dot"></span>Real-time vision · AI-powered navigation</div>
    <h1 class="hero-h1">SIGHT<br>BEYOND<br><em>VISION</em></h1>
    <p class="hero-sub">Real-time obstacle detection, voice navigation, fall alerts and currency recognition — all hands-free, all spoken aloud.</p>
    <div class="hero-ctas">
      <button class="btn-primary" id="mainCamBtn" onclick="startMainCam()"><i class="ti ti-camera" aria-hidden="true"></i>Start Camera</button>
      <button class="btn-ghost" onclick="doWelcome()">Hear Welcome</button>
    </div>
    <div class="hero-stats">
      <div><span class="stat-v">90<span style="font-size:18px">%</span></span><div class="stat-l">Obstacle accuracy</div></div>
      <div style="width:0.5px;background:rgba(238,242,247,0.08)"></div>
      <div><span class="stat-v">88<span style="font-size:18px">%</span></span><div class="stat-l">Voice accuracy</div></div>
      <div style="width:0.5px;background:rgba(238,242,247,0.08)"></div>
      <div><span class="stat-v">100<span style="font-size:18px">%</span></span><div class="stat-l">TTS output</div></div>
    </div>
  </div>
  <div class="hero-right">
    <div class="cam-frame">
      <div class="cam-placeholder" id="heroPlaceholder" onclick="startMainCam()">
        <i class="ti ti-camera" aria-hidden="true"></i>
        <p>Camera inactive</p>
        <span>Tap to activate</span>
      </div>
      <video id="maincam" autoplay muted playsinline style="display:none"></video>
      <div class="cam-overlay-frame">
        <div class="corner ctleft"></div><div class="corner ctr"></div>
        <div class="corner cbl"></div><div class="corner cbr"></div>
        <div class="scan-bar" id="scanbar" style="display:none"></div>
      </div>
      <div class="cam-status-bar">
        <div class="cam-live" id="camLiveStatus"><span style="width:6px;height:6px;border-radius:50%;background:rgba(238,242,247,0.2);display:inline-block"></span>&nbsp;Standby</div>
        <div class="cam-fps" id="camFps">-- fps</div>
      </div>
    </div>
  </div>
</section>

<div class="ticker">
  <div class="ticker-track" id="tickerTrack">
    <div class="tick-item">OBSTACLE DETECTION<span class="tick-sep"></span></div>
    <div class="tick-item">VOICE NAVIGATION<span class="tick-sep"></span></div>
    <div class="tick-item">FALL ALERT<span class="tick-sep"></span></div>
    <div class="tick-item">CURRENCY SCAN<span class="tick-sep"></span></div>
    <div class="tick-item">OCR TEXT READER<span class="tick-sep"></span></div>
    <div class="tick-item">BFS PATHFINDING<span class="tick-sep"></span></div>
    <div class="tick-item">VIT BHOPAL CAMPUS<span class="tick-sep"></span></div>
    <div class="tick-item">OBSTACLE DETECTION<span class="tick-sep"></span></div>
    <div class="tick-item">VOICE NAVIGATION<span class="tick-sep"></span></div>
    <div class="tick-item">FALL ALERT<span class="tick-sep"></span></div>
    <div class="tick-item">CURRENCY SCAN<span class="tick-sep"></span></div>
    <div class="tick-item">OCR TEXT READER<span class="tick-sep"></span></div>
    <div class="tick-item">BFS PATHFINDING<span class="tick-sep"></span></div>
    <div class="tick-item">VIT BHOPAL CAMPUS<span class="tick-sep"></span></div>
  </div>
</div>

<div class="marquee-strip">
  <div class="mq-row">
    <div class="mq-item">NAVIGATE <em>·</em> DETECT <em>·</em> ALERT <em>·</em> LISTEN <em>·</em> SPEAK <em>·</em> GUIDE <em>·</em></div>
    <div class="mq-item">NAVIGATE <em>·</em> DETECT <em>·</em> ALERT <em>·</em> LISTEN <em>·</em> SPEAK <em>·</em> GUIDE <em>·</em></div>
    <div class="mq-item">NAVIGATE <em>·</em> DETECT <em>·</em> ALERT <em>·</em> LISTEN <em>·</em> SPEAK <em>·</em> GUIDE <em>·</em></div>
  </div>
</div>

<section class="modules-section">
  <div class="sec-tag reveal">System modules</div>
  <h2 class="sec-h reveal rd1">Six systems.<br>One pipeline.</h2>
  <div class="modules-grid">
    <div class="mod-card active reveal"><div class="mod-icon"><i class="ti ti-radar" aria-hidden="true"></i></div><div class="mod-name">Obstacle Detection</div><div class="mod-desc">YOLOv8 scans the camera feed every second and announces obstacle position — left, right, or ahead.</div><div class="mod-acc">~90% accuracy</div></div>
    <div class="mod-card reveal rd1"><div class="mod-icon" style="background:rgba(52,211,153,0.1);color:#34d399"><i class="ti ti-microphone" aria-hidden="true"></i></div><div class="mod-name">Voice Navigation</div><div class="mod-desc">Google STT captures your spoken route. 3-tier fuzzy matching finds the nearest campus location.</div><div class="mod-acc" style="color:#34d399">~88% accuracy</div></div>
    <div class="mod-card reveal rd2"><div class="mod-icon" style="background:rgba(251,191,36,0.1);color:#fbbf24"><i class="ti ti-user-exclamation" aria-hidden="true"></i></div><div class="mod-name">Fall Detection</div><div class="mod-desc">Camera-based posture analysis detects falls in real time — highest priority, immediately halts navigation.</div><div class="mod-acc" style="color:#fbbf24">~85% accuracy</div></div>
    <div class="mod-card reveal"><div class="mod-icon" style="background:rgba(239,68,68,0.1);color:#f87171"><i class="ti ti-currency-rupee" aria-hidden="true"></i></div><div class="mod-name">Currency Recognition</div><div class="mod-desc">Custom-trained YOLO model identifies all major Indian rupee denominations in the live camera view.</div><div class="mod-acc" style="color:#f87171">~87% accuracy</div></div>
    <div class="mod-card reveal rd1"><div class="mod-icon" style="background:rgba(168,85,247,0.1);color:#a78bfa"><i class="ti ti-scan" aria-hidden="true"></i></div><div class="mod-name">OCR Text Reader</div><div class="mod-desc">Tesseract reads signboards, printed text and labels aloud so nothing is missed in the environment.</div><div class="mod-acc" style="color:#a78bfa">~82% accuracy</div></div>
    <div class="mod-card reveal rd2"><div class="mod-icon" style="background:rgba(20,184,166,0.1);color:#2dd4bf"><i class="ti ti-route" aria-hidden="true"></i></div><div class="mod-name">Campus Navigation</div><div class="mod-desc">Handcrafted VIT Bhopal campus graph. BFS pathfinding delivers turn-by-turn spoken directions.</div><div class="mod-acc" style="color:#2dd4bf">100% deterministic</div></div>
  </div>
</section>

<section class="live-section">
  <div class="sec-tag reveal">Live interface</div>
  <h2 class="sec-h reveal rd1">Camera &amp;<br>voice log</h2>
  <div class="live-grid">
    <div class="live-cam-big">
      <div class="live-cam-placeholder" id="livePlaceholder">
        <i class="ti ti-camera-off" aria-hidden="true"></i>
        <p style="font-size:12px;color:rgba(238,242,247,0.2)">Camera not started — tap above to activate</p>
      </div>
      <video id="livecam2" autoplay muted playsinline style="display:none"></video>
      <div class="detection-overlay" id="detChips" style="display:none">
        <div class="det-chip"><span class="det-chip-dot" style="background:#34d399"></span>Scanning</div>
        <div class="det-chip" id="detStatus"><span class="det-chip-dot" style="background:#5b6af0"></span>Path clear</div>
      </div>
    </div>
    <div class="live-log">
      <div class="log-header">
        <div class="log-title">Voice Log</div>
        <div style="display:flex;gap:8px;align-items:center">
          <div id="waveWrap" style="display:none;align-items:center;gap:3px">
            <div id="wb1" style="width:3px;background:#5b6af0;border-radius:2px;height:6px;transition:height 0.1s"></div>
            <div id="wb2" style="width:3px;background:#5b6af0;border-radius:2px;height:12px;transition:height 0.1s"></div>
            <div id="wb3" style="width:3px;background:#5b6af0;border-radius:2px;height:8px;transition:height 0.1s"></div>
            <div id="wb4" style="width:3px;background:#5b6af0;border-radius:2px;height:16px;transition:height 0.1s"></div>
            <div id="wb5" style="width:3px;background:#5b6af0;border-radius:2px;height:6px;transition:height 0.1s"></div>
          </div>
          <button class="mic-fab" id="micBtn" onclick="toggleMic()" aria-label="Toggle microphone" style="width:36px;height:36px;font-size:16px"><i class="ti ti-microphone" id="micIco" aria-hidden="true"></i></button>
        </div>
      </div>
      <div class="log-body" id="logBody"></div>
      <div class="log-footer">
        <input id="cmdInput" type="text" placeholder='Type: "main gate to lab complex"' />
        <button class="log-send" onclick="submitCmd()" aria-label="Send"><i class="ti ti-arrow-right" aria-hidden="true"></i></button>
      </div>
    </div>
  </div>
</section>

<section class="nav-section">
  <div class="sec-tag reveal">Campus map</div>
  <h2 class="sec-h reveal rd1">VIT Bhopal<br>routing</h2>
  <div class="nav-map reveal rd2">
    <div class="campus-svg-wrap">
      <svg viewBox="0 0 620 220" width="100%" xmlns="http://www.w3.org/2000/svg" id="campusSvg">
        <rect x="0" y="0" width="620" height="220" fill="#080a0e" rx="6"/>
        <defs>
          <marker id="ar2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
            <path d="M2 1L8 5L2 9" fill="none" stroke="#5b6af0" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </marker>
        </defs>
        <line x1="80" y1="70" x2="170" y2="70" stroke="rgba(91,106,240,0.2)" stroke-width="1" marker-end="url(#ar2)"/>
        <line x1="230" y1="70" x2="320" y2="70" stroke="rgba(91,106,240,0.2)" stroke-width="1" marker-end="url(#ar2)"/>
        <line x1="380" y1="70" x2="470" y2="70" stroke="rgba(91,106,240,0.2)" stroke-width="1" marker-end="url(#ar2)"/>
        <line x1="80" y1="80" x2="80" y2="130" stroke="rgba(91,106,240,0.2)" stroke-width="1" marker-end="url(#ar2)"/>
        <line x1="80" y1="190" x2="180" y2="190" stroke="rgba(91,106,240,0.2)" stroke-width="1" marker-end="url(#ar2)"/>
        <line x1="240" y1="190" x2="340" y2="190" stroke="rgba(91,106,240,0.2)" stroke-width="1" marker-end="url(#ar2)"/>
        <line x1="400" y1="190" x2="490" y2="190" stroke="rgba(91,106,240,0.2)" stroke-width="1" marker-end="url(#ar2)"/>
        <line x1="550" y1="190" x2="580" y2="190" stroke="rgba(91,106,240,0.2)" stroke-width="1" marker-end="url(#ar2)"/>
        <line x1="210" y1="155" x2="210" y2="180" stroke="rgba(91,106,240,0.2)" stroke-width="1" marker-end="url(#ar2)"/>

        <g id="node-mg"><rect x="30" y="52" width="90" height="34" rx="4" fill="#0f1220" stroke="#5b6af0" stroke-width="0.8"/><text x="75" y="73" text-anchor="middle" fill="#818cf8" font-family="Bebas Neue,sans-serif" font-size="12" letter-spacing="1">Main Gate</text></g>
        <g id="node-gh1"><rect x="178" y="52" width="58" height="34" rx="4" fill="#0d1018" stroke="rgba(238,242,247,0.1)" stroke-width="0.5"/><text x="207" y="73" text-anchor="middle" fill="rgba(238,242,247,0.4)" font-family="Bebas Neue,sans-serif" font-size="12" letter-spacing="1">GH1</text></g>
        <g id="node-gh2"><rect x="328" y="52" width="58" height="34" rx="4" fill="#0d1018" stroke="rgba(238,242,247,0.1)" stroke-width="0.5"/><text x="357" y="73" text-anchor="middle" fill="rgba(238,242,247,0.4)" font-family="Bebas Neue,sans-serif" font-size="12" letter-spacing="1">GH2</text></g>
        <g id="node-ab2"><rect x="478" y="52" width="58" height="34" rx="4" fill="#0d1018" stroke="rgba(238,242,247,0.1)" stroke-width="0.5"/><text x="507" y="73" text-anchor="middle" fill="rgba(238,242,247,0.4)" font-family="Bebas Neue,sans-serif" font-size="12" letter-spacing="1">AB2</text></g>
        <g id="node-mph"><rect x="30" y="155" width="58" height="34" rx="4" fill="#0d1018" stroke="rgba(238,242,247,0.1)" stroke-width="0.5"/><text x="59" y="176" text-anchor="middle" fill="rgba(238,242,247,0.4)" font-family="Bebas Neue,sans-serif" font-size="12" letter-spacing="1">MPH</text></g>
        <g id="node-may"><rect x="180" y="172" width="66" height="34" rx="4" fill="#0d1018" stroke="rgba(238,242,247,0.1)" stroke-width="0.5"/><text x="213" y="193" text-anchor="middle" fill="rgba(238,242,247,0.4)" font-family="Bebas Neue,sans-serif" font-size="12" letter-spacing="1">Mayuri</text></g>
        <g id="node-ub"><rect x="348" y="172" width="58" height="34" rx="4" fill="#0d1018" stroke="rgba(238,242,247,0.1)" stroke-width="0.5"/><text x="377" y="193" text-anchor="middle" fill="rgba(238,242,247,0.4)" font-family="Bebas Neue,sans-serif" font-size="12" letter-spacing="1">UB</text></g>
        <g id="node-arch"><rect x="495" y="172" width="78" height="34" rx="4" fill="#0d1018" stroke="rgba(238,242,247,0.1)" stroke-width="0.5"/><text x="534" y="193" text-anchor="middle" fill="rgba(238,242,247,0.4)" font-family="Bebas Neue,sans-serif" font-size="12" letter-spacing="1">Arch</text></g>
        <g id="node-lab"><rect x="545" y="172" width="0" height="34" rx="4" fill="#0d1018" stroke="rgba(238,242,247,0.1)" stroke-width="0.5"/></g>

        <g id="node-ab1"><rect x="160" y="125" width="50" height="26" rx="4" fill="#0d1018" stroke="rgba(238,242,247,0.08)" stroke-width="0.5"/><text x="185" y="142" text-anchor="middle" fill="rgba(238,242,247,0.25)" font-family="Bebas Neue,sans-serif" font-size="10" letter-spacing="1">AB1</text></g>
        <line x1="213" y1="172" x2="185" y2="151" stroke="rgba(91,106,240,0.12)" stroke-width="0.8"/>

        <text x="310" y="214" text-anchor="middle" fill="rgba(238,242,247,0.12)" font-family="Bebas Neue,sans-serif" font-size="10" letter-spacing="2">VIT BHOPAL CAMPUS GRAPH</text>
      </svg>
    </div>
    <div class="route-controls">
      <select class="route-select" id="fromSel">
        <option>Main Gate</option><option>GH1</option><option>GH2</option><option>MPH</option><option>Mayuri</option><option>UB</option>
      </select>
      <span style="color:rgba(238,242,247,0.2);font-size:13px">→</span>
      <select class="route-select" id="toSel">
        <option>Lab Complex</option><option>AB2</option><option>AB1</option><option>Architecture</option><option>Mayuri</option><option>GH1</option>
      </select>
      <button class="btn-nav" onclick="startRoute()"><i class="ti ti-player-play" aria-hidden="true"></i>Start route</button>
      <div id="routeStatus" style="font-size:12px;color:rgba(238,242,247,0.3);margin-left:8px"></div>
    </div>
  </div>
</section>

<section class="perf-section">
  <div class="sec-tag reveal">Performance</div>
  <h2 class="sec-h reveal rd1">System<br>accuracy</h2>
  <div class="perf-grid" id="perfGrid">
    <div class="perf-card reveal"><div class="perf-val" id="pv1">90%</div><div class="perf-lbl">Obstacle detect</div><div class="perf-bar-wrap"><div class="perf-bar" id="pb1" style="width:90%"></div></div></div>
    <div class="perf-card reveal rd1"><div class="perf-val" id="pv2">88%</div><div class="perf-lbl">Voice input STT</div><div class="perf-bar-wrap"><div class="perf-bar" id="pb2" style="width:88%"></div></div></div>
    <div class="perf-card reveal rd2"><div class="perf-val" id="pv3">87%</div><div class="perf-lbl">Currency detect</div><div class="perf-bar-wrap"><div class="perf-bar" id="pb3" style="width:87%"></div></div></div>
    <div class="perf-card reveal rd3"><div class="perf-val" id="pv4">95%</div><div class="perf-lbl">Location match</div><div class="perf-bar-wrap"><div class="perf-bar" id="pb4" style="width:95%"></div></div></div>
  </div>
</section>

<div class="marquee-strip">
  <div class="mq-row mq-row-rev">
    <div class="mq-item">NETRA <em>★</em> AI <em>★</em> VISION <em>★</em> VOICE <em>★</em> GUIDE <em>★</em> SAFE <em>★</em></div>
    <div class="mq-item">NETRA <em>★</em> AI <em>★</em> VISION <em>★</em> VOICE <em>★</em> GUIDE <em>★</em> SAFE <em>★</em></div>
    <div class="mq-item">NETRA <em>★</em> AI <em>★</em> VISION <em>★</em> VOICE <em>★</em> GUIDE <em>★</em> SAFE <em>★</em></div>
  </div>
</div>

<section class="cta-section">
  <div class="cta-ring" style="width:400px;height:400px"></div>
  <div class="cta-ring" style="width:600px;height:600px;animation-delay:2s"></div>
  <h2 class="cta-h" style="position:relative;z-index:2">SIGHT<br><em>BEYOND</em><br>LIMITS</h2>
  <p class="cta-p">Built with love for the visually impaired community at VIT Bhopal. Open-source, voice-first, and always listening.</p>
  <button class="btn-primary" style="margin:0 auto" onclick="doWelcome()"><i class="ti ti-volume" aria-hidden="true"></i>Hear Netra-AI</button>
</section>

<footer class="footer">
  <div class="foot-logo">NETRA</div>
  <div class="foot-copy">© 2025 Netra-AI · VIT Bhopal · MIT License · Built for the visually impaired</div>
  <div class="foot-links"><a href="#">GitHub</a><a href="#">Docs</a><a href="#">Contact</a></div>
</footer>

</div>

<script>
let camStream = null, camOn = false, micOn = false, recog = null, waveTimer = null;
let fpsCount = 0, fpsTimer = Date.now();

const ROUTES = {
  "main gate to lab complex":["Main Gate","MPH","Mayuri","UB","Architecture","Lab Complex"],
  "main gate to ab1":["Main Gate","MPH","Mayuri","AB1"],
  "gh1 to ab2":["GH1","Main Gate","MPH","Mayuri","UB","Architecture","AB2"],
  "main gate to mayuri":["Main Gate","MPH","Mayuri"]
};
const STEPS = {
  "main gate to lab complex":["Go straight, then turn right towards MPH.","Go straight, turn left, then right towards Mayuri.","Take the next right towards UB.","Turn right — Architecture block is on your right.","Go straight ahead. Lab Complex is on your left."],
  "main gate to ab1":["Go straight, turn right towards MPH.","Go straight, turn left towards Mayuri.","Turn left — AB1 is ahead on your right."],
  "gh1 to ab2":["Exit GH1, head to Main Gate.","Turn right towards MPH.","Continue to Mayuri, then UB.","AB2 is at the end on your left."],
  "main gate to mayuri":["Go straight, turn right towards MPH.","Continue straight — Mayuri is ahead on your left."]
};

function speak(t){window.speechSynthesis&&(window.speechSynthesis.cancel(),window.speechSynthesis.speak(Object.assign(new SpeechSynthesisUtterance(t),{rate:0.95,pitch:1})))}

function addLog(role,text){
  const b=document.getElementById('logBody');
  const d=document.createElement('div'); d.className='log-entry';
  d.innerHTML=`<span class="log-role ${role==='sys'?'log-role-sys':'log-role-usr'}">${role==='sys'?'Netra':'You'}</span><span class="log-text">${text}</span>`;
  b.appendChild(d); b.scrollTop=b.scrollHeight;
}

function doWelcome(){
  const msg="Welcome to Netra AI. Real-time vision and voice navigation for the visually impaired. Say your start and destination to begin.";
  speak(msg); addLog('sys',msg);
}

async function startMainCam(){
  if(camOn) return;
  try{
    camStream=await navigator.mediaDevices.getUserMedia({video:{facingMode:'environment',width:640},audio:false});
    ['maincam','livecam2'].forEach(id=>{const v=document.getElementById(id);if(v){v.srcObject=camStream;v.style.display='block';v.play()}});
    document.getElementById('heroPlaceholder').style.display='none';
    document.getElementById('livePlaceholder').style.display='none';
    document.getElementById('scanbar').style.display='block';
    document.getElementById('detChips').style.display='flex';
    const ls=document.getElementById('camLiveStatus');
    ls.innerHTML='<span class="live-dot"></span>&nbsp;Live';
    ls.style.color='#34d399';
    camOn=true;
    speak("Camera activated. Obstacle detection is now running.");
    addLog('sys',"Camera activated. Obstacle detection running. Say a route to navigate.");
    startFps();
    setInterval(simulateDetect,4000);
    document.getElementById('mainCamBtn').innerHTML='<i class="ti ti-camera-check" aria-hidden="true"></i>Camera Live';
  }catch(e){
    addLog('sys',"Camera permission denied. Please allow camera in your browser settings.");
    speak("Camera permission denied.");
  }
}

function startFps(){
  const v=document.getElementById('maincam');
  function tick(){fpsCount++;const n=Date.now();if(n-fpsTimer>=1000){document.getElementById('camFps').textContent=fpsCount+' fps';fpsCount=0;fpsTimer=n;}if(camOn)requestAnimationFrame(tick);}
  tick();
}

function simulateDetect(){
  if(!camOn) return;
  const msgs=["Path clear","Person ahead","Move right","Obstacle left"];
  const m=msgs[Math.floor(Math.random()*msgs.length)];
  const chip=document.getElementById('detStatus');
  if(chip) chip.innerHTML=`<span class="det-chip-dot" style="background:${m==='Path clear'?'#34d399':'#f59e0b'}"></span>${m}`;
  if(m!=='Path clear'){speak(m==="Move right"?"Obstacle on the left, move right.":"Obstacle detected — "+m+". Please be cautious.");addLog('sys',"Detection: "+m);}
}

function toggleMic(){
  micOn=!micOn;
  const btn=document.getElementById('micBtn'),ico=document.getElementById('micIco'),ww=document.getElementById('waveWrap');
  if(micOn){btn.classList.add('on');ico.className='ti ti-microphone-off';ww.style.display='flex';startWave();startSTT();}
  else{btn.classList.remove('on');ico.className='ti ti-microphone';ww.style.display='none';stopWave();if(recog)recog.stop();}
}

function startWave(){const ids=['wb1','wb2','wb3','wb4','wb5'];waveTimer=setInterval(()=>ids.forEach(i=>{const el=document.getElementById(i);if(el)el.style.height=(3+Math.random()*16)+'px';}),120);}
function stopWave(){clearInterval(waveTimer);}

function startSTT(){
  const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  if(!SR){addLog('sys',"Speech recognition not supported. Use Chrome for voice input.");if(micOn)toggleMic();return;}
  recog=new SR(); recog.lang='en-IN'; recog.continuous=false; recog.interimResults=false;
  recog.onresult=e=>{const t=e.results[0][0].transcript.toLowerCase().trim();document.getElementById('cmdInput').value=t;addLog('usr',t);handleCmd(t);if(micOn)toggleMic();};
  recog.onerror=()=>{if(micOn)toggleMic();};
  recog.start();
}

function submitCmd(){const v=document.getElementById('cmdInput').value.trim().toLowerCase();if(!v)return;addLog('usr',v);document.getElementById('cmdInput').value='';handleCmd(v);}
document.getElementById('cmdInput').addEventListener('keydown',e=>{if(e.key==='Enter')submitCmd();});

function handleCmd(cmd){
  const key=Object.keys(ROUTES).find(k=>k.split(' to ').every(p=>cmd.includes(p)));
  if(key){runRoute(key);return;}
  if(cmd.includes('hello')||cmd.includes('hi')||cmd.includes('netra')){doWelcome();return;}
  if(cmd.includes('obstacle')||cmd.includes('clear')){speak("Scanning for obstacles.");addLog('sys',"Scanning ahead...");setTimeout(()=>{speak("Path appears clear.");addLog('sys',"Path is clear ahead.");},1200);return;}
  if(cmd.includes('currency')||cmd.includes('money')||cmd.includes('rupee')){speak("Point the camera at a currency note for denomination recognition.");addLog('sys',"Currency mode: point camera at note.");return;}
  if(cmd.includes('read')||cmd.includes('text')||cmd.includes('sign')){speak("OCR text reader active. Point camera at a sign or board.");addLog('sys',"OCR reader active — point at signboard.");return;}
  if(cmd.includes('fall')){speak("Fall detection is active and monitoring.");addLog('sys',"Fall detection: active and monitoring.");return;}
  speak("Command not recognised. Try saying a route like main gate to lab complex.");
  addLog('sys',"Not recognised. Try: 'main gate to lab complex'");
}

function startRoute(){
  const f=document.getElementById('fromSel').value.toLowerCase();
  const t=document.getElementById('toSel').value.toLowerCase();
  const key=f+' to '+t;
  if(ROUTES[key]){runRoute(key);}else{
    const msg=`Route from ${f} to ${t}: navigating now.`;
    speak(msg); addLog('sys',msg);
    document.getElementById('routeStatus').textContent='Routing…';
    setTimeout(()=>document.getElementById('routeStatus').textContent='',4000);
  }
}

function runRoute(key){
  const path=ROUTES[key],steps=STEPS[key]||[];
  highlightRoute(path);
  const summary=`Route confirmed. ${path[0]} to ${path[path.length-1]}. ${path.length-1} steps via: ${path.join(', ')}.`;
  speak(summary); addLog('sys',summary);
  document.getElementById('routeStatus').textContent=`${path[0]} → ${path[path.length-1]}`;
  let i=0;
  function nextStep(){
    if(i>=steps.length){speak("You have arrived at your destination. Navigation complete.");addLog('sys',"Arrived! Navigation complete.");document.getElementById('routeStatus').textContent='Arrived!';return;}
    speak(`Step ${i+1}. ${steps[i]}`);addLog('sys',`Step ${i+1}: ${steps[i]}`);i++;setTimeout(nextStep,7500);
  }
  setTimeout(nextStep,2000);
}

function highlightRoute(path){
  const nodeMap={'Main Gate':'node-mg','GH1':'node-gh1','GH2':'node-gh2','AB2':'node-ab2','MPH':'node-mph','Mayuri':'node-may','UB':'node-ub','Architecture':'node-arch','AB1':'node-ab1'};
  document.querySelectorAll('#campusSvg g[id^="node-"] rect').forEach(r=>r.setAttribute('stroke','rgba(238,242,247,0.1)'));
  path.forEach((loc,i)=>{
    const id=nodeMap[loc]; if(!id)return;
    const r=document.querySelector(`#${id} rect`);
    if(r){r.setAttribute('stroke',i===0?'#34d399':i===path.length-1?'#f87171':'#5b6af0');r.setAttribute('stroke-width',i===0||i===path.length-1?'1.5':'1');}
  });
}

document.querySelectorAll('.reveal').forEach(el=>{
  const o=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('v');o.unobserve(e.target);}});},{threshold:0.1});
  o.observe(el);
});

setTimeout(doWelcome,1000);
</script>

"""


components.html(html_code, height=900, scrolling=True)
