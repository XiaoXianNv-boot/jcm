
function main() {
    let reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
    let r = window.location.search.substr(1).match(reg);
    if (r != null) {
//        location.href = 'home.html?link=' + r[2];
    };
//    document.getElementById('biaotou').innerHTML = “集群管理”;

    if (document.body.clientWidth <= 600) {
        str = '<tr>'
        str += '  <th class="detail-col" >'
        str += '    <label class="pos-rel">'
        str += '      <input type="checkbox" class="ace" />'
        str += '      <span class="lbl"></span>'
        str += '    </label>'
        str += '  </th >'
        str += '  <th class="">节点名称</th>'
        str += '  <th class="detail-col">受控端</th>'
        //str += '  <th class="detail-col">安全</th>'
        //str += '  <th class="hidden-480">CPU</th>'
        //str += '  <th class="hidden-480">内存</th>'
        //str += '  <th class="hidden-480">存储</th>'
        //str += '  <th class="hidden-480">网络</th>'
        str += '  <th class="">操作</th>'
        str += '</tr >'
        document.getElementById('biaotou1').innerHTML = str;
    }
    up_biao();
    window.setInterval(up_biao, 1000);
    //pj();
    //window.setInterval(pj, 1000);
}

function up_biao() {
    var ys = document.getElementById('sxx').innerText;
    if (ys == 1) {
        document.getElementById('sxx').innerText = 0;
        const Http = new XMLHttpRequest();
        Http.open("GET", 'main/info?arg=upbiao');
        Http.send();
        Http.onreadystatechange = (e) => {
            var readyState = Http.readyState;
            var status = Http.status;
            if (readyState == 4 && status == 401) {
                location.reload();
            }
            if (readyState == 4 && status == 200) {
                cathttp = Http.responseText;
                if (cathttp.substr(0, 1) == "<") {
                    location.reload();
                } else {
                    var data = JSON.parse(cathttp);
                    var up = 0
                    if (document.body.clientWidth <= 600) {//判断页面大小
                        str = '<tr>'
                        str += '  <th class="detail-col" >'
                        str += '    <label class="pos-rel">'
                        str += '      <input type="checkbox" class="ace" />'
                        str += '      <span class="lbl"></span>'
                        str += '    </label>'
                        str += '  </th >'
                        str += '  <th class="">节点名称</th>'
                        str += '  <th class="detail-col">受控端</th>'
                        //str += '  <th class="detail-col">安全</th>'
                        //str += '  <th class="hidden-480">CPU</th>'
                        //str += '  <th class="hidden-480">内存</th>'
                        //str += '  <th class="hidden-480">存储</th>'
                        //str += '  <th class="hidden-480">网络</th>'
                        str += '  <th class="">操作</th>'
                        str += '</tr >'
                        document.getElementById('biaotou1').innerHTML = str;

                        for (i = 0; i < data.for; i++) {
                            servername = data.server[i].name
                            servername = servername.replace('.', '_')
                            servername = servername.replace('.', '_')
                            servername = servername.replace('.', '_')
                            servername = servername.replace('.', '_')
                            var s = document.getElementById(servername + "mini");
                            if (s) {//是否存在此设备信息
                                if (data.server[i].api == "0") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-warning">离线</span>' }
                                if (data.server[i].api == "1") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-success">在线</span>' }
                                if (data.server[i].api == "2") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-inverse">未安装</span>' }
                                if (data.server[i].api == "3") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-danger ">登录失败</span>' }
                            } else {
                                up++;
                            }
                        }
                        if (up > 0) {//重写列表
                            var reg = "";
                            var link = "";
                            for (i = 0; i < data.for; i++) {
                                servername = data.server[i].name
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                if (data.server[i].name == "127.0.0.1") {
                                    link = "./";
                                } else {
                                    link = "http://" + data.server[i].name + ":8889/";
                                }
                                reg = reg + '<tr>';
                                reg = reg + '<td class="center">';
                                reg = reg + '<label class="pos-rel">';
                                reg = reg + '<input type="checkbox" class="ace" />';
                                reg = reg + '<span class="lbl"></span>';
                                reg = reg + '</label>';
                                reg = reg + '</td>';
                                reg = reg + '<td>';
                                reg = reg + '<a href="info?link=' + data.server[i].name + '" id="' + servername + "mini" + '">' + data.server[i].name + '</a>';
                                reg = reg + '</td>';
                                reg = reg + '<td id="' + servername + "api" + '">';
                                reg = reg + '</td>';
                                reg = reg + '<td>\
                                    <div class="hidden-sm hidden-xs btn-group" >\
                                            <button class="btn btn-xs btn-success">\
                                                <i class="ace-icon fa fa-check bigger-120"></i>\
                                            </button>\
                                    \
                                            <button class="btn btn-xs btn-info">\
                                                <i class="ace-icon fa fa-pencil bigger-120"></i>\
                                            </button>\
                                    \
                                            <button class="btn btn-xs btn-danger">\
                                                <i class="ace-icon fa fa-trash-o bigger-120"></i>\
                                            </button>\
                                    \
                                            <button class="btn btn-xs btn-warning">\
                                                <i class="ace-icon fa fa-flag bigger-120"></i>\
                                            </button>\
                                        </div >\
                                    \
                                    <div class="hidden-md hidden-lg">\
                                        <div class="inline pos-rel">\
                                            <button class="btn btn-minier btn-primary dropdown-toggle" data-toggle="dropdown" data-position="auto">\
                                                <i class="ace-icon fa fa-cog icon-only bigger-110"></i>\
                                            </button>\
                                    \
                                            <ul class="dropdown-menu dropdown-only-icon dropdown-yellow dropdown-menu-right dropdown-caret dropdown-close">\
                                                <li>\
                                                    <a href="#" class="tooltip-info" data-rel="tooltip" title="View">\
                                                        <span class="blue">\
                                                            <i class="ace-icon fa fa-search-plus bigger-120"></i>\
                                                        </span>\
                                                    </a>\
                                                </li>\
                                    \
                                                <li>\
                                                    <a href="#" class="tooltip-success" data-rel="tooltip" title="Edit">\
                                                        <span class="green">\
                                                            <i class="ace-icon fa fa-pencil-square-o bigger-120"></i>\
                                                        </span>\
                                                    </a>\
                                                </li>\
                                    \
                                                <li>\
                                                    <a href="#" class="tooltip-error" data-rel="tooltip" title="Delete">\
                                                        <span class="red">\
                                                            <i class="ace-icon fa fa-trash-o bigger-120"></i>\
                                                        </span>\
                                                    </a>\
                                                </li>\
                                            </ul>\
                                        </div>\
                                    </div>\
                                    </td >';
                                reg = reg + '</tr>';
                                reg = reg + '';
                            }
                            document.getElementById("biaoinfo").innerHTML = reg;
                            for (i = 0; i < data.for; i++) {
                                servername = data.server[i].name
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                var s = document.getElementById(servername + "mini");
                                if (s) {//是否存在此设备信息
                                    if (data.server[i].api == "0") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-warning">离线</span>' }
                                    if (data.server[i].api == "1") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-success">在线</span>' }
                                    if (data.server[i].api == "2") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-inverse">未安装</span>' }
                                    if (data.server[i].api == "3") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-danger ">登录失败</span>' }
                                } else {
                                    up++;
                                }
                            }
                        }
                    } else {
                        str = '<tr>'
                        str += '  <th class="detail-col" >'
                        str += '    <label class="pos-rel">'
                        str += '      <input type="checkbox" class="ace" />'
                        str += '      <span class="lbl"></span>'
                        str += '    </label>'
                        str += '  </th >'
                        str += '  <th class="">节点名称</th>'
                        str += '  <th class="detail-col">受控端</th>'
                        str += '  <th class="detail-col">安全</th>'
                        str += '  <th class="col-sm-1" style="width: 15%;">CPU</th>'
                        str += '  <th class="col-sm-2" style="width: 15%;">内存</th>'
                        str += '  <th class="col-sm-2" style="width: 15%;">存储</th>'
                        str += '  <th class="">网络</th>'
                        str += '  <th class="">操作</th>'
                        str += '</tr >'
                        document.getElementById('biaotou1').innerHTML = str;

                        for (i = 0; i < data.for; i++) {
                            servername = data.server[i].name
                            servername = servername.replace('.', '_')
                            servername = servername.replace('.', '_')
                            servername = servername.replace('.', '_')
                            servername = servername.replace('.', '_')
                            var s = document.getElementById(servername);
                            if (s) {
                                if (data.server[i].api == "0") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-warning">离线</span>' }
                                if (data.server[i].api == "1") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-success">在线</span>' }
                                if (data.server[i].api == "2") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-inverse">未安装</span>' }
                                if (data.server[i].api == "3") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-danger ">登录失败</span>' }
                                document.getElementById(servername + "safe").innerHTML = data.server[i].safe
                                jdta = document.getElementById(servername + "cpua");
                                jdtb = document.getElementById(servername + "cpub");
                                $("#" + servername + "cpua").attr("data-percent", data.server[i].cpu + "%")
                                jdtb.style = "width:" + data.server[i].cpu + "%;";
                                if (data.server[i].cpu < 30) {
                                    jdtb.className = "progress-bar progress-bar-success";
                                } else if (data.server[i].cpu < 50) {
                                    jdtb.className = "progress-bar";
                                } else if (data.server[i].cpu < 80) {
                                    jdtb.className = "progress-bar progress-bar-warning";
                                } else {
                                    jdtb.className = "progress-bar progress-bar-danger";
                                }
                                jdta = document.getElementById(servername + "rama");
                                jdtb = document.getElementById(servername + "ramb");
                                $("#" + servername + "rama").attr("data-percent", data.server[i].ram + "%")
                                jdtb.style = "width:" + data.server[i].ram + "%;";
                                if (data.server[i].ram < 30) {
                                    jdtb.className = "progress-bar progress-bar-success";
                                } else if (data.server[i].ram < 50) {
                                    jdtb.className = "progress-bar";
                                } else if (data.server[i].ram < 80) {
                                    jdtb.className = "progress-bar progress-bar-warning";
                                } else {
                                    jdtb.className = "progress-bar progress-bar-danger";
                                }
                                var jdta = document.getElementById(servername + "roma");
                                var jdtb = document.getElementById(servername + "romb");
                                $("#" + servername + "roma").attr("data-percent", data.server[i].rom + "%")
                                jdtb.style = "width:" + data.server[i].rom + "%;";
                                if (data.server[i].rom < 30) {
                                    jdtb.className = "progress-bar progress-bar-success";
                                } else if (data.server[i].rom < 50) {
                                    jdtb.className = "progress-bar";
                                } else if (data.server[i].rom < 80) {
                                    jdtb.className = "progress-bar progress-bar-warning";
                                } else {
                                    jdtb.className = "progress-bar progress-bar-danger";
                                }
                                document.getElementById(servername + "net").innerHTML = '<i class="ace-icon glyphicon glyphicon-upload"></i>' + data.server[i].tx + '<i class="ace-icon glyphicon glyphicon-download"></i>' + data.server[i].rx
                            } else {
                                up++;
                            }

                        }
                        if (up > 0) {
                            var reg = "";
                            var link = "";
                            for (i = 0; i < data.for; i++) {
                                servername = data.server[i].name
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                if (data.server[i].name == "127.0.0.1") {
                                    link = "./";
                                } else {
                                    link = "http://" + data.server[i].name + ":8889/";
                                }
                                reg = reg + '<tr>';
                                reg = reg + '<td class="center">';
                                reg = reg + '<label class="pos-rel">';
                                reg = reg + '<input type="checkbox" class="ace" />';
                                reg = reg + '<span class="lbl"></span>';
                                reg = reg + '</label>';
                                reg = reg + '</td>';
                                reg = reg + '<td>';
                                reg = reg + '<a href="info?link=' + data.server[i].name + '" id="' + servername + '">' + data.server[i].name + '</a>';
                                reg = reg + '</td>';
                                reg = reg + '<td id="' + servername + "api" + '">';
                                reg = reg + '</td>';
                                reg = reg + '<td class="" id="' + servername + "safe" + '"></td>';
                                reg = reg + '<td>';
                                //reg = reg + '<!--div class="progress">';
                                //reg = reg + '<div class="progress-bar progress-bar-danger" style="width: 0%;" id="' + servername + "cpua" + '"></div>';
                                //reg = reg + '<div class="progress-bar progress-bar-warning" style="width: 0%;" id="' + servername + "cpub" + '"></div>';
                                //reg = reg + '<div class="progress-bar progress-bar-success" style="width: 0%;" id="' + servername + "cpuc" + '"></div>';
                                //reg = reg + '</div-->';
                                reg = reg + '<div class="progress pos-rel" data-percent="0%" id="' + servername + "cpua" + '">';
                                reg = reg + '<div class="progress-bar" style="width:0%;" id="' + servername + "cpub" + '"></div>';
                                reg = reg + '</div>'
                                reg = reg + '</td>';
                                reg = reg + '<td class="">';
                                reg = reg + '<div class="progress pos-rel" data-percent="0%" id="' + servername + "rama" + '">';
                                reg = reg + '<div class="progress-bar" style="width:0%;" id="' + servername + "ramb" + '"></div>';
                                reg = reg + '</div>';
                                reg = reg + '</td>';
                                reg = reg + '<td class="">';
                                reg = reg + '<div class="progress pos-rel" data-percent="0%" id="' + servername + "roma" + '">';
                                reg = reg + '<div class="progress-bar" style="width:0%;" id="' + servername + "romb" + '"></div>';
                                reg = reg + '</div>';
                                reg = reg + '</td>';
                                reg = reg + '<td id="' + servername + "net" + '"></td>';
                                reg = reg + '<td>\
                                    没写<!--div class="hidden-sm hidden-xs btn-group" >\
                                            <button class="btn btn-xs btn-success">\
                                                <i class="ace-icon fa fa-check bigger-120"></i>\
                                            </button>\
                                    \
                                            <button class="btn btn-xs btn-info">\
                                                <i class="ace-icon fa fa-pencil bigger-120"></i>\
                                            </button>\
                                    \
                                            <button class="btn btn-xs btn-danger">\
                                                <i class="ace-icon fa fa-trash-o bigger-120"></i>\
                                            </button>\
                                    \
                                            <button class="btn btn-xs btn-warning">\
                                                <i class="ace-icon fa fa-flag bigger-120"></i>\
                                            </button>\
                                        </div >\
                                    \
                                    <div class="hidden-md hidden-lg">\
                                        <div class="inline pos-rel">\
                                            <button class="btn btn-minier btn-primary dropdown-toggle" data-toggle="dropdown" data-position="auto">\
                                                <i class="ace-icon fa fa-cog icon-only bigger-110"></i>\
                                            </button>\
                                    \
                                            <ul class="dropdown-menu dropdown-only-icon dropdown-yellow dropdown-menu-right dropdown-caret dropdown-close">\
                                                <li>\
                                                    <a href="#" class="tooltip-info" data-rel="tooltip" title="View">\
                                                        <span class="blue">\
                                                            <i class="ace-icon fa fa-search-plus bigger-120"></i>\
                                                        </span>\
                                                    </a>\
                                                </li>\
                                    \
                                                <li>\
                                                    <a href="#" class="tooltip-success" data-rel="tooltip" title="Edit">\
                                                        <span class="green">\
                                                            <i class="ace-icon fa fa-pencil-square-o bigger-120"></i>\
                                                        </span>\
                                                    </a>\
                                                </li>\
                                    \
                                                <li>\
                                                    <a href="#" class="tooltip-error" data-rel="tooltip" title="Delete">\
                                                        <span class="red">\
                                                            <i class="ace-icon fa fa-trash-o bigger-120"></i>\
                                                        </span>\
                                                    </a>\
                                                </li>\
                                            </ul>\
                                        </div>\
                                    </div-->\
                                    </td >';
                                reg = reg + '</tr>';
                                reg = reg + '';
                            }
                            document.getElementById("biaoinfo").innerHTML = reg;
                            for (i = 0; i < data.for; i++) {
                                servername = data.server[i].name
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                var s = document.getElementById(servername);
                                if (s) {
                                    if (data.server[i].api == "0") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-warning">离线</span>' }
                                    if (data.server[i].api == "1") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-success">在线</span>' }
                                    if (data.server[i].api == "2") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-inverse">未安装</span>' }
                                    if (data.server[i].api == "3") { document.getElementById(servername + "api").innerHTML = '<span class="label label-sm label-danger ">登录失败</span>' }
                                    document.getElementById(servername + "safe").innerHTML = data.server[i].safe
                                    var jdta = document.getElementById(servername + "cpua");
                                    var jdtb = document.getElementById(servername + "cpub");
                                    var jdtc = document.getElementById(servername + "cpuc");
                                    var jdtd = document.getElementById(servername + "cpud");
                                    $("#" + servername + "cpua").attr("data-percent", data.server[i].cpu0 + "%")
                                    jdtb.style = "width:" + data.server[i].cpu0 + "%;";
                                    //jdtc.style = "width:" + data.server[i].cpu1 + "%;";
                                    jdtd.style = "width:" + data.server[i].cpu1 + "%;";
                                    jdtc.style = "width: 0%;";
                                    //var jdta = document.getElementById(servername + "cpua");
                                    //var jdtb = document.getElementById(servername + "cpub");
                                    //$("#" + servername + "cpua").attr("data-percent", data.server[i].cpu + "%")
                                    //jdtb.style = "width:" + data.server[i].cpu + "%;";
                                    /*if (data.server[i].cpu < 30) {
                                        jdtb.className = "progress-bar progress-bar-success";
                                    } else if (data.server[i].cpu < 50) {
                                        jdtb.className = "progress-bar";
                                    } else if (data.server[i].cpu < 80) {
                                        jdtb.className = "progress-bar progress-bar-warning";
                                    } else {
                                        jdtb.className = "progress-bar progress-bar-danger";
                                    }*/
                                    jdta = document.getElementById(servername + "rama");
                                    jdtb = document.getElementById(servername + "ramb");
                                    $("#" + servername + "rama").attr("data-percent", data.server[i].ram + "%")
                                    jdtb.style = "width:" + data.server[i].ram + "%;";
                                    if (data.server[i].ram < 30) {
                                        jdtb.className = "progress-bar progress-bar-success";
                                    } else if (data.server[i].ram < 50) {
                                        jdtb.className = "progress-bar";
                                    } else if (data.server[i].ram < 80) {
                                        jdtb.className = "progress-bar progress-bar-warning";
                                    } else {
                                        jdtb.className = "progress-bar progress-bar-danger";
                                    }
                                    var jdta = document.getElementById(servername + "roma");
                                    var jdtb = document.getElementById(servername + "romb");
                                    $("#" + servername + "roma").attr("data-percent", data.server[i].rom + "%")
                                    jdtb.style = "width:" + data.server[i].rom + "%;";
                                    if (data.server[i].rom < 30) {
                                        jdtb.className = "progress-bar progress-bar-success";
                                    } else if (data.server[i].rom < 50) {
                                        jdtb.className = "progress-bar";
                                    } else if (data.server[i].rom < 80) {
                                        jdtb.className = "progress-bar progress-bar-warning";
                                    } else {
                                        jdtb.className = "progress-bar progress-bar-danger";
                                    }
                                    document.getElementById(servername + "net").innerHTML = '<i class="ace-icon glyphicon glyphicon-upload"></i>' + data.server[i].tx + '<i class="ace-icon glyphicon glyphicon-download"></i>' + data.server[i].rx
                                } else {
                                    up++;
                                }

                            }
                        }
                    }
                }
            }

            document.getElementById('sxx').innerText = 1;
        }
    } else if (ys > 1) {
        document.getElementById('sxx').innerText = document.getElementById('sxx').innerText - 1;
    }
}

main();