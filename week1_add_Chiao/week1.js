// ==事件處理一:靜態的寫法========================================
//<<<<事件處理:觸發A，則會產生B>>>>
//【特性】
// 1. 對象:有兩個A、B
// 2. 動作:A->點擊/ 動作:B->CSS的變化
// 【執行步驟】
// html:
// 1. 找到觸發對象A-> 事件處理(事件)函式(處理函式)
// 2. 找到反應對象B-> 給他標籤名稱id
// CSS:
// 1. 反應對象B-> html中新增class選擇器
// 2. 樣式設定-> 切換的樣式 /display:none
// js:
// 1. 撰寫事件處理函式
// 2. 函式中:取得A-B連結/ document.getElementById(標籤名稱id)
// 3. 函式中:使用切換工具/ classList.toggle("class選擇器")

function toggleMenu(){
    var menu=document.getElementById("menu");
    // classList.toggle("class選擇器")
    menu.classList.toggle("hide")
}
// --------------------------------
function toggleItems(number){
    var items=document.getElementById("items-"+number);
    items.classList.toggle("items-hide");
}

// ==事件處理:動頁的寫法(註冊事件處理器)========================================
// function init(){
//     var js_Menu=document.getElementById("js_Menu");
//     var menu=document.getElementById("menu");
//     var toggleMenu=function(){
//         menu.classList.toggle("hide");
//     }
//     js_Menu.addEventListener("click",toggleMenu);
//     //--------------------------------
//     var js_Items=document.getElementById("js_Items");
//     var items=document.getElementById("items");//產品簡介的id要改(id無法寫兩個?)，
//     var toggleItems=function(){
//         items.classList.toggle("items-hide");
//     }
//     js_Items.addEventListener("click",toggleItems);
//     //是否可以透過參數設定來處理三個選單的開合功能?
        //事件處理器body中onload="init()"設定後，RWD的功能會消失(待處理)
// }

