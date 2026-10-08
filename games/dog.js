/* SnoutsWise original cartoon dog (inline SVG). (c) 2026 Joshua Israel Ventures LLC. Original code and art. */
window.SWDog=function(o){o=o||{};var C={fur:'#F5A54A',dark:'#1A1633',belly:'#FFE3B8',ear:'#C96A1E',tongue:'#FF6F91',white:'#FFFFFF'};
var low=o.low||0,by=118+low,bx=150,s='',q=function(t){s+=t};
var hx=222,hy=by-30;if(o.head=='up'){hx=226;hy=by-44}if(o.head=='low'){hx=230;hy=by+2}
var leg=function(x,top,len,rot){return '<rect x="'+(x-9)+'" y="'+top+'" width="18" height="'+len+'" rx="9" fill="'+C.fur+'" stroke="'+C.dark+'" stroke-width="3"'+(rot?' transform="rotate('+rot+' '+x+' '+top+')"':'')+'/>'};
var tb={x:bx-68,y:by-10},tp;
if(o.tail=='high')tp='M'+tb.x+','+tb.y+' Q'+(tb.x-16)+','+(tb.y-30)+' '+(tb.x-10)+','+(tb.y-60);
else if(o.tail=='tucked')tp='M'+tb.x+','+tb.y+' Q'+(tb.x-14)+','+(tb.y+30)+' '+(tb.x+18)+','+(tb.y+46);
else tp='M'+tb.x+','+tb.y+' Q'+(tb.x-30)+','+(tb.y-8)+' '+(tb.x-52)+','+(tb.y+6);
var cls=o.tail=='heli'?'heli':(o.wag=='none'||!o.wag?'':'wag '+o.wag);
if(o.tail=='heli')tp='M'+tb.x+','+tb.y+' Q'+(tb.x-26)+','+(tb.y-22)+' '+(tb.x-44)+','+(tb.y-30);
q('<svg viewBox="0 0 320 210" role="img" aria-label="'+(o.label||'Cartoon dog')+'" xmlns="http://www.w3.org/2000/svg">');
q('<ellipse cx="160" cy="194" rx="120" ry="9" fill="#1A1633" opacity=".12"/>');
var g0=o.bow?'<g transform="rotate(14 100 150)">':'<g>';q(g0);
q('<g class="'+cls+'" style="transform-origin:'+tb.x+'px '+tb.y+'px"><path d="'+tp+'" stroke="'+C.dark+'" stroke-width="17" fill="none" stroke-linecap="round"/><path d="'+tp+'" stroke="'+C.fur+'" stroke-width="11" fill="none" stroke-linecap="round"/></g>');
var lt=by+16,ll=Math.max(18,190-lt);
q(leg(108,lt,ll,0)+leg(128,lt,ll,0));
q('<ellipse cx="'+bx+'" cy="'+by+'" rx="72" ry="36" fill="'+C.fur+'" stroke="'+C.dark+'" stroke-width="3"/>');
q('<ellipse cx="'+(bx+6)+'" cy="'+(by+18)+'" rx="46" ry="12" fill="'+C.belly+'"/>');
if(o.hackles){var hp='M112,'+(by-30);for(var i=0;i<8;i++)hp+=' l6,-12 l6,12';q('<path d="'+hp+'" fill="'+C.fur+'" stroke="'+C.dark+'" stroke-width="3" stroke-linejoin="round"/>')}
if(!o.bow){q(leg(182,lt,ll,0));q(o.paw?leg(200,lt,30,-55):leg(200,lt,ll,0))}
q('<ellipse cx="'+(bx+52)+'" cy="'+(Math.min(by-12,hy+16))+'" rx="24" ry="'+(o.head=='low'?20:28)+'" fill="'+C.fur+'" stroke="'+C.dark+'" stroke-width="3"/>');
var ear='';
if(o.ears=='up')ear='M'+(hx-16)+','+(hy-18)+' L'+(hx-6)+','+(hy-64)+' L'+(hx+10)+','+(hy-22)+' Z';
else if(o.ears=='back')ear='M'+(hx-4)+','+(hy-26)+' L'+(hx-46)+','+(hy-30)+' L'+(hx-12)+','+(hy-12)+' Z';
else if(o.ears=='flat')ear='M'+(hx-2)+','+(hy-22)+' L'+(hx-44)+','+(hy-16)+' L'+(hx-6)+','+(hy-10)+' Z';
else ear='M'+(hx-14)+','+(hy-22)+' Q'+(hx-34)+','+(hy-4)+' '+(hx-22)+','+(hy+16)+' Q'+(hx-6)+','+(hy+2)+' '+(hx+2)+','+(hy-26)+' Z';
q('<circle cx="'+hx+'" cy="'+hy+'" r="30" fill="'+C.fur+'" stroke="'+C.dark+'" stroke-width="3"/>');
q('<path d="'+ear+'" fill="'+C.ear+'" stroke="'+C.dark+'" stroke-width="3" stroke-linejoin="round"/>');
q('<ellipse cx="'+(hx+30)+'" cy="'+(hy+10)+'" rx="23" ry="14" fill="'+C.belly+'" stroke="'+C.dark+'" stroke-width="3"/>');
var ex=hx+8,ey=hy-6;
if(o.eye=='whale')q('<ellipse cx="'+ex+'" cy="'+ey+'" rx="9" ry="7" fill="#fff" stroke="'+C.dark+'" stroke-width="2"/><circle cx="'+(ex-5)+'" cy="'+ey+'" r="3.5" fill="'+C.dark+'"/>');
else if(o.eye=='hard')q('<circle cx="'+ex+'" cy="'+ey+'" r="6.5" fill="'+C.dark+'"/><path d="M'+(ex-9)+','+(ey-13)+' L'+(ex+9)+','+(ey-7)+'" stroke="'+C.dark+'" stroke-width="4" stroke-linecap="round"/>');
else if(o.eye=='away')q('<ellipse cx="'+ex+'" cy="'+ey+'" rx="7" ry="5" fill="#fff" stroke="'+C.dark+'" stroke-width="2"/><circle cx="'+(ex-3)+'" cy="'+(ey+2)+'" r="3" fill="'+C.dark+'"/>');
else q('<path d="M'+(ex-7)+','+ey+' Q'+ex+','+(ey-7)+' '+(ex+7)+','+ey+'" stroke="'+C.dark+'" stroke-width="3.5" fill="none" stroke-linecap="round"/>');
q('<ellipse cx="'+(hx+50)+'" cy="'+(hy+4)+'" rx="7" ry="6" fill="'+C.dark+'"/>');
var m=o.mouth;
if(m=='open')q('<path d="M'+(hx+22)+','+(hy+18)+' Q'+(hx+38)+','+(hy+36)+' '+(hx+52)+','+(hy+16)+' Z" fill="'+C.dark+'"/><ellipse cx="'+(hx+38)+'" cy="'+(hy+30)+'" rx="7" ry="9" fill="'+C.tongue+'" stroke="'+C.dark+'" stroke-width="2"/>');
else if(m=='yawn')q('<ellipse cx="'+(hx+38)+'" cy="'+(hy+24)+'" rx="12" ry="14" fill="'+C.dark+'"/><ellipse cx="'+(hx+38)+'" cy="'+(hy+32)+'" rx="6" ry="4" fill="'+C.tongue+'"/>');
else if(m=='teeth'){q('<path d="M'+(hx+16)+','+(hy+15)+' L'+(hx+56)+','+(hy+12)+' L'+(hx+54)+','+(hy+25)+' L'+(hx+18)+','+(hy+23)+' Z" fill="'+C.dark+'"/>');for(var t=0;t<5;t++)q('<path d="M'+(hx+22+t*7)+','+(hy+14)+' l3.5,7 l3.5,-7 Z" fill="#fff"/>')}
else{q('<path d="M'+(hx+12)+','+(hy+19)+' Q'+(hx+36)+','+(hy+23)+' '+(hx+50)+','+(hy+16)+'" stroke="'+C.dark+'" stroke-width="3" fill="none" stroke-linecap="round"/>');if(m=='lick')q('<ellipse cx="'+(hx+54)+'" cy="'+(hy+13)+'" rx="4.5" ry="7" fill="'+C.tongue+'" stroke="'+C.dark+'" stroke-width="2"/>')}
if(o.wrinkle)q('<path d="M'+(hx+24)+','+(hy-1)+' q4,-4 8,0 M'+(hx+32)+','+(hy-3)+' q4,-4 8,0 M'+(hx+40)+','+(hy-1)+' q4,-4 8,0" stroke="'+C.dark+'" stroke-width="2.5" fill="none" stroke-linecap="round"/>');
q('</g>');
if(o.bow){q('<rect x="196" y="175" width="62" height="16" rx="8" fill="'+C.fur+'" stroke="'+C.dark+'" stroke-width="3"/><rect x="186" y="178" width="58" height="14" rx="7" fill="'+C.fur+'" stroke="'+C.dark+'" stroke-width="3"/>')}
q('</svg>');return s};
