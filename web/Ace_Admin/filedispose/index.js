

function addindir(){
    const Http = new XMLHttpRequest();
    var dir = $('input[name=addindir]').val();
    var rul = catrul("filedispose/indir/add?");
    Http.open("GET",rul + '&dir=' + dir);
    Http.send();
    Http.onreadystatechange = (e) => {
        if(Http.readyState == 4){
            //if (Http.status == 200) {
                bootbox.confirm(Http.responseText, function (result) {
                    catindir();
                })
            //}
        }
    }
}
function catindir(){
    const Http = new XMLHttpRequest();
    var rul = catrul("filedispose/indir/info?");
    Http.open("GET",rul);
    Http.send();
    Http.onreadystatechange = (e) => {
        if(Http.readyState == 4){
            if (Http.status == 200) {
                var data = JSON.parse(Http.responseText);
                document.getElementById('biaoinfoinml').innerHTML = '';
                for (i = 0;i < data.fo;i++){
                    var res = '';
                    res += '<tr>';
                    res += '<td class="center"><label class="pos-rel"><input type="checkbox" class="ace"><span class="lbl"></span></label></td>';
                    res += '<td >' + data.data[i].dir + '</td>';
                    res += '<td >' + data.data[i].status + '</td>';
                    res += '<td >' + '' + '</td>';
                    res += '</tr>';
                    document.getElementById('biaoinfoinml').innerHTML += res;
                }
            }
        }
    }
}

function addoutdir(){
    const Http = new XMLHttpRequest();
    var dir = $('input[name=addoutdir]').val();
    var name = $('input[name=name]').val();
    var rul = catrul("filedispose/outdir/add?");
    Http.open("GET",rul + '&dir=' + dir + '&name=' + name);
    Http.send();
    Http.onreadystatechange = (e) => {
        if(Http.readyState == 4){
            //if (Http.status == 200) {
                bootbox.confirm(Http.responseText, function (result) {
                    catoutdir();
                })
            //}
        }
    }
}
function catoutdir(){
    const Http = new XMLHttpRequest();
    var rul = catrul("filedispose/outdir/info?");
    Http.open("GET",rul);
    Http.send();
    Http.onreadystatechange = (e) => {
        if(Http.readyState == 4){
            if (Http.status == 200) {
                var data = JSON.parse(Http.responseText);
                document.getElementById('biaoinfooutml').innerHTML = '';
                for (i = 0;i < data.fo;i++){
                    var res = '';
                    res += '<tr>';
                    res += '<td class="center"><label class="pos-rel"><input type="checkbox" class="ace"><span class="lbl"></span></label></td>';
                    res += '<td >' + data.data[i].name + '</td>';
                    res += '<td >' + data.data[i].dir + '</td>';
                    res += '<td >' + data.data[i].Size + '</td>';
                    res += '<td >' + data.data[i].status + '</td>';
                    res += '<td >' + '' + '</td>';
                    res += '</tr>';
                    document.getElementById('biaoinfooutml').innerHTML += res;
                }
            }
        }
    }
}
function addddir(){
    const Http = new XMLHttpRequest();
    var dir = $('input[name=ddir]').val();
    var name = $('input[name=dname]').val();
    var rul = catrul("filedispose/default/add?");
    Http.open("GET",rul + '&dir=' + dir + '&name=' + name);
    Http.send();
    Http.onreadystatechange = (e) => {
        if(Http.readyState == 4){
            //if (Http.status == 200) {
                bootbox.confirm(Http.responseText, function (result) {
                    catdefaultdir();
                })
            //}
        }
    }
}
function catdefaultdir(){
    const Http = new XMLHttpRequest();
    var rul = catrul("filedispose/default/info?");
    Http.open("GET",rul);
    Http.send();
    Http.onreadystatechange = (e) => {
        if(Http.readyState == 4){
            if (Http.status == 200) {
                var data = JSON.parse(Http.responseText);
                document.getElementById('biaoinfod').innerHTML = '';
                for (i = 0;i < data.fo;i++){
                    var res = '';
                    res += '<tr>';
                    res += '<td class="center"><label class="pos-rel"><input type="checkbox" class="ace"><span class="lbl"></span></label></td>';
                    res += '<td >' + data.data[i].dir + '</td>';
                    res += '<td >' + data.data[i].name + '</td>';
                    res += '<td >' + '' + '</td>';
                    res += '</tr>';
                    document.getElementById('biaoinfod').innerHTML += res;
                }
            }
        }
    }
}

function run(){
    var wsrul = '';
    var ifdata = document.getElementById("linktext").innerHTML;
    if(ifdata == "断开"){
        document.getElementById("tab1nn").className = "";
        document.getElementById("tab2nn").className = " active ";
        document.getElementById("tab1n").className = "tab-pane fade";
        document.getElementById("tab2n").className = "tab-pane fade active in";
        document.getElementById("linktext").innerHTML = "正在连接";
        if (window.location.protocol == 'http:') { wsrul = 'ws://'; } else if (window.location.protocol == 'https:') { wsrul = 'wss://'; }
        var ws = new WebSocket(wsrul + window.location.host + "/filedispose/filenocopy");
        ws.onopen = function (evt) {
            document.getElementById("linktext").innerHTML = "连接";
            document.getElementById("runtext").innerHTML = "0";
            document.getElementById("runtextx").innerHTML = "";
            document.getElementById("biaoinfo").innerHTML = ""; 
            document.getElementById("data").innerHTML = '';   
        }    
        ws.onclose = function (evt) {
            document.getElementById("linktext").innerHTML = "断开";
            document.getElementById("runtextx").innerHTML = "/ " + document.getElementById("runtext").innerHTML;
        }
        ws.onmessage = function (evt) {
            console.log(evt.data)
            var ifdata;
            ifdata = evt.data.slice(-2);
            if(ifdata == "\r\n"){
                var evtdata = document.getElementById("data").innerHTML + evt.data;
                document.getElementById("data").innerHTML = '';
                ifdata = evtdata.slice(0,2);
                if(ifdata == 'n '){
                    var dir;
                    var res;
                    ifdata = evtdata.slice(2);
                    res = ifdata.split('\r');
                    dir = res[0].split('\t');
                    res = '';
                    res += '<tr>';
                    res += '<td class="center"><label class="pos-rel"><input type="checkbox" class="ace"><span class="lbl"></span></label></td>';
                    res += '<td >' + dir[0] + '</td>';
                    res += '<td >\
                    <input class=" input-sm" type="text" \
                    id="' + document.getElementById("runtext").innerHTML + '" \
                    name="' + document.getElementById("runtext").innerHTML + '" \
                    value="' + dir[1] + '">\
                    <input type="hidden" \
                    id="' + document.getElementById("runtext").innerHTML + 'n" \
                    name="' + document.getElementById("runtext").innerHTML + 'n" \
                    value="' + dir[2] + '"></td>';
                    res += '<td id="' + document.getElementById("runtext").innerHTML + 'd">' + '\
                    <button class=" btn btn-sm " \
                    onclick="diron(' + "'" + document.getElementById("runtext").innerHTML + "'" + ');">\
                    确认\
                    </button>\
                    ' + '</td>';
                    res += '</tr>';
                    document.getElementById('biaoinfo').innerHTML += res;
                    document.getElementById("runtext").innerHTML = Number(document.getElementById("runtext").innerHTML) + 1;
                }else if(ifdata == 'f '){
                    var dir;
                    var res;
                    ifdata = evtdata.slice(2);
                    res = ifdata.split('\r');
                    dir = res[0].split('\t');
                    res = '';
                    res += '<tr>';
                    res += '<td class="center"><label class="pos-rel"><input type="checkbox" class="ace"><span class="lbl"></span></label></td>';
                    res += '<td >' + dir[0] + '</td>';
                    res += '<td >' + dir[1] + '</td>';
                    res += '<td id="' + document.getElementById("runtext").innerHTML + 'd">' + "" + '</td>';
                    document.getElementById('biaoinfo').innerHTML += res;
                    document.getElementById("runtext").innerHTML = Number(document.getElementById("runtext").innerHTML) + 1;

                }
            }else{
                document.getElementById("data").innerHTML += evt.data;
            }
        }
    }else{
        bootbox.confirm("上一个进程未结束", function (result) {
        })
    }
}

function mv(){
    var wsrul = '';
    var ifdata = document.getElementById("linktext").innerHTML;
    if(ifdata == "断开"){
        document.getElementById("linktext").innerHTML = "正在连接";
        if (window.location.protocol == 'http:') { wsrul = 'ws://'; } else if (window.location.protocol == 'https:') { wsrul = 'wss://'; }
        var ws = new WebSocket(wsrul + window.location.host + "/filedispose/filemd5cp");
        ws.onopen = function (evt) {
            document.getElementById("linktext").innerHTML = "连接";
            document.getElementById("runtext").innerHTML = "0";
            document.getElementById("biaoinfo").innerHTML = "";  
            document.getElementById("data").innerHTML = '';  
        }    
        ws.onclose = function (evt) {
            document.getElementById("linktext").innerHTML = "断开";
        }
        ws.onmessage = function (evt) {
            var ifdata;
            ifdata = evt.data.slice(-2);
            if(ifdata == "\r\n"){
                var evtdata = document.getElementById("data").innerHTML + evt.data;
                document.getElementById("data").innerHTML = '';
                ifdata = evtdata.slice(0,2);
                if(ifdata == 'b '){
                    ifdata = evtdata.slice(2);
                    res = ifdata.split('\r');
                    dir = res[0].split('\t');

                    var id = Number(document.getElementById("runtext").innerHTML) - 1;
                    document.getElementById(id + 'd').innerHTML = res[0];
                }else{
                    console.log(evtdata)
                    if(ifdata == 'f '){
                        var dir;
                        var res;
                        ifdata = evtdata.slice(2);
                        res = ifdata.split('\r');
                        dir = res[0].split('\t');
                        res = '';
                        res += '<tr>';
                        res += '<td class="center"><label class="pos-rel"><input type="checkbox" class="ace"><span class="lbl"></span></label></td>';
                        res += '<td >' + dir[0] + '</td>';
                        res += '<td >' + dir[1] + '</td>';
                        res += '<td id="' + document.getElementById("runtext").innerHTML + 'd">' + "" + '</td>';
                        document.getElementById('biaoinfo').innerHTML = res + document.getElementById('biaoinfo').innerHTML;
                        document.getElementById("runtext").innerHTML = Number(document.getElementById("runtext").innerHTML) + 1;
                    }
                }

            }else{
                document.getElementById("data").innerHTML += evt.data;
            }
        }

    }else{
        bootbox.confirm("上一个进程未结束", function (result) {
        })
    }

}

function diron(lis){
    var dir = $('input[name=' + lis + ']').val();
    var name = $('input[name=' + lis + 'n]').val();
    const Http = new XMLHttpRequest();
    var rul = catrul("filedispose/filenocopy/add?");
    Http.open("POST",rul);
    Http.send("" + '{"name":"' + name + '","dir":"' + dir + '","id":"' + lis + '"}');
    Http.onreadystatechange = (e) => {
        if(Http.readyState == 4){
            if (Http.status == 200) {
                var data = JSON.parse(Http.responseText);
                document.getElementById(data.id + 'd').innerHTML = data.data;
            }
        }
    }
}

catindir();
catoutdir();
catdefaultdir();