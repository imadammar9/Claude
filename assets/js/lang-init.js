/* Runs in <head> before paint: pick the language from ?lang=, saved choice, or the browser. */
(function(){try{var u=new URL(location.href),q=u.searchParams.get('lang'),s=null;try{s=localStorage.getItem('tadawa.lang')}catch(e){}var b=(navigator.language||'').toLowerCase().indexOf('ar')===0?'ar':'en';var l=(q==='ar'||q==='en')?q:(s==='ar'||s==='en')?s:b;document.documentElement.setAttribute('lang',l);document.documentElement.setAttribute('dir',l==='ar'?'rtl':'ltr');}catch(e){}})();

/* Always open a page at the top (unless the link targets a section) */
(function(){try{if('scrollRestoration' in history)history.scrollRestoration='manual';}catch(e){}
function top(){if(location.hash&&location.hash.length>1&&document.getElementById(location.hash.slice(1)))return;var h=document.documentElement,b=h.style.scrollBehavior;h.style.scrollBehavior='auto';window.scrollTo(0,0);h.style.scrollBehavior=b;}
top();document.addEventListener('DOMContentLoaded',top);window.addEventListener('load',function(){top();setTimeout(top,60);});window.addEventListener('pageshow',function(e){if(e.persisted)top();});})();
