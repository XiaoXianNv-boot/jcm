function catrul(rul) {
    const Http = new XMLHttpRequest();
    var reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    if (r == null) {
        r = ["link=127.0.0.1", 0, 0];
    }
    //Http.open(rul + '')
    return rul + r[0];
}


function jcminit() {
    const Http = new XMLHttpRequest();
    //let rul = window.location.pathname;
    Http.open("GET", "main/biao");
    Http.send();
    Http.onreadystatechange = (e) => {
        if (Http.readyState == 4 && Http.status == 200) {
            var data = JSON.parse(Http.responseText);
            var str = '';
            var reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
            var r = window.location.search.substr(1).match(reg);
            if (r == null){
                r = [0,0,0];
            }
            str += '<li class="">';
            str += '<a href="./">';
            str += '<i class="menu-icon fa fa-tachometer"></i>';
            str += '<span class="menu-text"> 集群管理 </span>';
            str += '</a>';
            str += '<b class="arrow"></b>';
            str += '</li>';
            for (i = 0; i < Object.keys(data.data).length; i++) {
                if (r[2] == data.data[i].name) {
                    str += '<li class="active open">';
                } else {
                    str += '<li class="">';
                }
                str += '<a href="#" class="dropdown-toggle">';
                str += '<i class="menu-icon fa fa-desktop"></i>';
                str += '<span class="menu-text"> ' + data.data[i].name + ' </span>';
                str += '<b class="arrow fa fa-angle-down"></b>';
                str += '</a>';
                str += '<b class="arrow"></b>';
                str += '<ul class="submenu">';
                for (j = 1; j < Object.keys(data.data[i].data).length; j++) {
                    if (r[2] == data.data[i].name) {
                        if (window.location.pathname + '?' == data.data[i].data[j - 1].link) {
                            str += '<li class="active">';
                        } else {
                            str += '<li class="">';
                        }
                    } else {
                        str += '<li class="">';
                    }
                    str += '<a href="' + data.data[i].data[j - 1].link + 'link=' + data.data[i].name + '">';
                    str += '<i class="menu-icon fa fa-caret-right"></i>';
                    str += '<span class="menu-text">  ' + data.data[i].data[j - 1].name + '  </span>';
                    str += '</a>';
                    str += '<b class="arrow"></b>';
                    str += '</li>';
                }
                str += '</ul>';
                str += '</li>';

            }
            document.getElementById('biao').innerHTML = str;
        }
    }
}
jcminit();




