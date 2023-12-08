window.onload = function () {
    infoupdata_();
}
window.setInterval(infoupdata, 10000);

function infoupdata_(){
    const cpuHttp = new XMLHttpRequest();
    cpuHttp.open("GET", 'info/info');
    cpuHttp.send();
    cpuHttp.onreadystatechange = function() {
        if(cpuHttp.readyState == 4 && cpuHttp.status == 200){
            var data = JSON.parse(cpuHttp.responseText);
            var str = '';
            servername = 'cpumain_';
            if (data.cpumain < 50) {
                document.getElementById(servername + 'c').style = "";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.cpumain).options.barColor = '#3983C2';
            } else if (data.cpumain < 80) {
                document.getElementById(servername + 'c').style = "color: orange;";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.cpumain).options.barColor = 'orange';
            } else {
                document.getElementById(servername + 'c').style = "color: brown;";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.cpumain).options.barColor = 'brown';
            }
            document.getElementById(servername + 'text').innerHTML = data.cputemp + '℃' + "";
            document.getElementById(servername + 't').innerHTML = data.cpumain + "";
            servername = 'rammain_';
            if (data.ram[0].ram < 50) {
                document.getElementById(servername + 'c').style = "";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.ram[0].ram).options.barColor = '#3983C2';
            } else if (data.ram[0].ram < 80) {
                document.getElementById(servername + 'c').style = "color: orange;";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.ram[0].ram).options.barColor = 'orange';
            } else {
                document.getElementById(servername + 'c').style = "color: brown;";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.ram[0].ram).options.barColor = 'brown';
            }
            //document.getElementById(servername + 'text').innerHTML = data.cputemp + '℃' + "";
            document.getElementById(servername + 't').innerHTML = data.ram[0].ram + "";
            servername = 'rommain_';
            if (data.rommain < 50) {
                document.getElementById(servername + 'c').style = "";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.rommain).options.barColor = '#3983C2';
            } else if (data.rommain < 80) {
                document.getElementById(servername + 'c').style = "color: orange;";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.rommain).options.barColor = 'orange';
            } else {
                document.getElementById(servername + 'c').style = "color: brown;";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.rommain).options.barColor = 'brown';
            }
            document.getElementById(servername + 'text').innerHTML = data.romnamemain + "";
            document.getElementById(servername + 't').innerHTML = data.rommain + "";

            servername = 'batmain_';
            if (data.bat != 0){
                if (data.bat < 50) {
                    document.getElementById(servername + 'c').style = "";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.bat).options.barColor = '#3983C2';
                } else if (data.bat < 80) {
                    document.getElementById(servername + 'c').style = "color: orange;";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.bat).options.barColor = 'orange';
                } else {
                    document.getElementById(servername + 'c').style = "color: brown;";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.bat).options.barColor = 'brown';
                }
                document.getElementById(servername + 'text').innerHTML = data.bat + "";
                document.getElementById(servername + 't').innerHTML = data.bat + "";
            }

            for (i = 0; i < data.cpufo; i++) {
                servername = data.cpu[i].name.replace(' ', '_')
                var ccol = '';
                var col = '';
                if (data.cpu[i].cpu < 50) {
                    ccol = "color: rgb(0, 128, 0);";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    col = '#3983C2';
                } else if (data.cpu[i].cpu < 80) {
                    ccol = "color: orange;";
                    col = 'orange';
                } else {
                    ccol = "color: rgb(255, 0, 0);";
                    col = 'brown';
                }
                str += '<div id="' + servername + 'c" class="infobox infobox-blue2" style="' + ccol + '">';
                str += '                <div class="infobox-progress">';
                str += '                    <div id="' + servername + '" class="easy-pie-chart percentage" data-percent="' + data.cpu[i].cpu + '" data-size="46">';
                str += '                        <span class="percent" id="' + servername + 't">' + data.cpu[i].cpu + '</span>%';
                str += '                    </div>';
                str += '                </div>';
                str += '';
                str += '                <div class="infobox-data">';
                str += '                    <span class="infobox-text">' + data.cpu[i].name + '</span>';
                str += '';
                str += '                    <div class="infobox-content">';
                str += '                        <span id="' + servername + 'f" class="bigger-110"> ' + data.cpu[i].freq + ' Mhz</span>';
                str += '                        ';
                str += '                    </div>';
                str += '                </div>';
                str += '            </div>';
            }
            document.getElementById('cpuinfotxt').innerHTML = 'CPU: ' + data.cpu[0].cpuname;
            document.getElementById('cpuinfo').innerHTML = str;
            update();
            var str = '';
            for (i = 0; i < data.ramfo; i++) {
                servername = data.ram[i].name.replace(' ', '_')
                var ccol = '';
                var col = '';
                if (data.ram[i].ram < 50) {
                    ccol = "color: rgb(0, 128, 0);";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    col = '#3983C2';
                } else if (data.ram[i].ram < 80) {
                    ccol = "color: orange;";
                    col = 'orange';
                } else {
                    ccol = "color: rgb(255, 0, 0);";
                    col = 'brown';
                }
                /**
                 * <div class="progress pos-rel" data-percent="66%">
													<div class="progress-bar" style="width:66%;"></div>
												</div>
                 */
                str += '<div id="' + servername + 'c" class="infobox infobox-blue2" style="' + ccol + '">';
                str += '                <div class="infobox-progress">';
                str += '                    <div id="' + servername + '" class="easy-pie-chart percentage" data-percent="' + data.ram[i].ram + '" data-size="46">';
                str += '                        <span class="percent" id="' + servername + 't">' + data.ram[i].ram + '</span>%';
                str += '                    </div>';
                str += '                </div>';
                str += '';
                str += '                <div class="infobox-data">';
                str += '                    <span class="infobox-text">' + data.ram[i].name + '</span>';
                str += '';
                str += '                    <div class="infobox-content">';
                str += '                        <span id="' + servername + 'i" class="bigger-110"> </span>';
                str += '                        ';
                str += '                    </div>';
                str += '                </div>';
                str += '            </div>';
            }
            document.getElementById('raminfo').innerHTML =str;
            update();
            var str = '';
            var p = '';
            p += '<p id="diskinfotext" class="alert alert-info" >';
            for (i = 0; i < data.disksmfo; i++) {
                servername = data.disksm[i].name.replace('/', '_')
                servername = servername.replace('/', '_')
                servername = servername.replace('/', '_')
                servername = servername.replace('/', '_')
                servername = servername + i
                var col = '';
                if (data.disksm[i].disk < 50){
                    col = "progress-bar-success";
                } else if (data.disksm[i].disk < 85) {
                    col = "";
                } else if (data.disksm[i].disk < 95) {
                    col = "progress-bar-warning";
                } else {
                    col = "progress-bar-danger";
                }
                str += '<div class"text" id="' + servername + "\">";
                str += data.disksm[i].diskinfo + "<br>";
                str += "</div>"
                str += '<div class="progress pos-rel" data-percent="'+ data.disksm[i].disk + '%" id="' + servername + "diska" + '">';
                str += '<div class="progress-bar ' + col + '" style="width:'+ data.disksm[i].disk + '%;" id="' + servername + "diskb" + '"></div>';
                str += '</div>';

                
                p += data.disksm[i].name + ' ' + data.disksm[i].diskinfo + "<br>";
            }
            for (i = 0; i < data.diskfo; i++) {
                servername = data.disk[i].name.replace('/', '_')
                servername = servername.replace('/', '_')
                servername = servername.replace('/', '_')
                servername = servername.replace('/', '_')
                servername = servername + i
                var col = '';
                if (data.disk[i].disk < 30){
                    col = "progress-bar-success";
                } else if (data.disk[i].disk < 50) {
                    col = "";
                } else if (data.disk[i].disk < 80) {
                    col = "progress-bar-warning";
                } else {
                    col = "progress-bar-danger";
                }
                str += '<div class"text" id="' + servername + "\">";
                str += data.disk[i].name + ' ' + data.disk[i].diskinfo + "<br>";
                str += "</div>"
                str += '<div class="progress pos-rel" data-percent="'+ data.disk[i].disk + '%" id="' + servername + "diska" + '">';
                str += '<div class="progress-bar ' + col + '" style="width:'+ data.disk[i].disk + '%;" id="' + servername + "diskb" + '"></div>';
                str += '</div>';
                /*
                str += '<div id="' + servername + 'c" class="infobox infobox-blue2" style="color: brown;">';
                str += '                <div class="infobox-progress">';
                str += '                    <div id="' + servername + '" class="easy-pie-chart percentage" data-percent="' + data.disk[i].disk + '" data-size="46">';
                str += '                        <span class="percent" id="' + servername + 't">' + data.disk[i].disk + '</span>%';
                str += '                    </div>';
                str += '                </div>';
                str += '';
                str += '                <div class="infobox-data">';
                str += '                    <span class="infobox-text">' + data.disk[i].name + '</span>';
                str += '';
                str += '                    <div class="infobox-content">';
                str += '                        <span id="' + servername + 'i" class="bigger-110"> </span>';
                str += '                        ';
                str += '                    </div>';
                str += '                </div>';
                str += '            </div>';*/
                p += data.disk[i].name + ' ' + data.disk[i].diskinfo + "<br>";
            }
            p += '</p>';
            p = ''
            document.getElementById('diskinfo').innerHTML = p + str;
            update();
        }
    }
    //infoupdata();
}

function infoupdata(){
    const cpuHttp = new XMLHttpRequest();
    cpuHttp.open("GET", 'info/info');
    cpuHttp.send();
    cpuHttp.onreadystatechange = function() {
        if(cpuHttp.readyState == 4 && cpuHttp.status == 200){
            var data = JSON.parse(cpuHttp.responseText);
            servername = 'cpumain_';
            if (data.cpumain < 50) {
                document.getElementById(servername + 'c').style = "";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.cpumain).options.barColor = '#3983C2';
            } else if (data.cpumain < 80) {
                document.getElementById(servername + 'c').style = "color: orange;";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.cpumain).options.barColor = 'orange';
            } else {
                document.getElementById(servername + 'c').style = "color: brown;";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.cpumain).options.barColor = 'brown';
            }
            document.getElementById(servername + 'text').innerHTML = data.cputemp + '℃' + "";
            document.getElementById(servername + 't').innerHTML = data.cpumain + "";
            servername = 'rammain_';
            if (data.ram[0].ram < 50) {
                document.getElementById(servername + 'c').style = "";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.ram[0].ram).options.barColor = '#3983C2';
            } else if (data.ram[0].ram < 80) {
                document.getElementById(servername + 'c').style = "color: orange;";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.ram[0].ram).options.barColor = 'orange';
            } else {
                document.getElementById(servername + 'c').style = "color: brown;";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.ram[0].ram).options.barColor = 'brown';
            }
            //document.getElementById(servername + 'text').innerHTML = data.cputemp + '℃' + "";
            document.getElementById(servername + 't').innerHTML = data.ram[0].ram + "";
            servername = 'rommain_';
            if (data.rommain < 50) {
                document.getElementById(servername + 'c').style = "";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.rommain).options.barColor = '#3983C2';
            } else if (data.rommain < 80) {
                document.getElementById(servername + 'c').style = "color: orange;";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.rommain).options.barColor = 'orange';
            } else {
                document.getElementById(servername + 'c').style = "color: brown;";
                //var $box = $('#' + servername).closest('.infobox');
                //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                $('#' + servername).data('easyPieChart').update(data.rommain).options.barColor = 'brown';
            }
            document.getElementById(servername + 'text').innerHTML = data.romnamemain + "";
            document.getElementById(servername + 't').innerHTML = data.rommain + "";

            servername = 'batmain_';
            if (data.bat != 0){
                if (data.bat < 10) {
                    document.getElementById(servername + 'c').style = "color: brown;";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.bat).options.barColor = 'brown';
                } else if (data.bat < 20) {
                    document.getElementById(servername + 'c').style = "color: orange;";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.bat).options.barColor = 'orange';
                } else {
                    document.getElementById(servername + 'c').style = "";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.bat).options.barColor = '#3983C2';
                }
                document.getElementById(servername + 'text').innerHTML =   "BAT";
                document.getElementById(servername + 't').innerHTML = data.bat + "";
            }

            //console.log(data);
            //var str = '';
            if (data.cputemp < 50) {
                document.getElementById('cpuwd').style = "background-color: #82AF6F;";
            } else if (data.cputemp < 90) {
                document.getElementById('cpuwd').style = "background-color: #F89406;";
            } else {
                document.getElementById('cpuwd').style = "background-color: #D15B47;";
            }
            document.getElementById('cpuwd').innerHTML = data.cputemp + '℃';
            for (i = 0; i < data.cpufo; i++) {
                servername = data.cpu[i].name.replace(' ', '_')
                
                //var s = document.getElementById(servername);
                //$("#" + servername + "A").attr("data-percent", data.cpu[i].cpu + '%')
                //document.getElementById(servername + "B").style = "width:" + data.cpu[i].cpu + "%;";
                if (data.cpu[i].cpu < 30) {
                    document.getElementById(servername + 'c').style = "color: #008000;";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.cpu[i].cpu).options.barColor = '#008000';
                } else if (data.cpu[i].cpu < 50) {
                    document.getElementById(servername + 'c').style = "color: #66ccff;";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.cpu[i].cpu).options.barColor = '#66ccff';
                } else if (data.cpu[i].cpu < 80) {
                    document.getElementById(servername + 'c').style = "color: #ffcc66;";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.cpu[i].cpu).options.barColor = '#ffcc66';
                } else {
                    document.getElementById(servername + 'c').style = "color: #f00;";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.cpu[i].cpu).options.barColor = '#f00';
                }
                document.getElementById(servername + 't').innerHTML = data.cpu[i].cpu + "";
                document.getElementById(servername + 'f').innerHTML = data.cpu[i].freq + "Mhz";
            }
            //document.getElementById('cpuinfo').innerHTML = str;
            //update();
            
    //    }
    //}
    //const ramHttp = new XMLHttpRequest();
    //ramHttp.open("GET", 'info/ram');
    //ramHttp.send();
    //ramHttp.onreadystatechange = function() {
    //    if(ramHttp.readyState == 4 && ramHttp.status == 200){
    //        var data = JSON.parse(ramHttp.responseText);
            for (i = 0; i < data.ramfo; i++) {
                servername = data.ram[i].name.replace(' ', '_')
                //var s = document.getElementById(servername);
                //$("#" + servername + "A").attr("data-percent", data.ram[i].ram + '%')
                //document.getElementById(servername + "B").style = "width:" + data.ram[i].ram + "%;";
                //document.getElementById(servername + "info").innerHTML = data.ram[i].raminfo;
                if (data.ram[i].ram < 30) {
                    document.getElementById(servername + 'c').style = "color: #008000;";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.ram[i].ram).options.barColor = '#008000';
                } else if (data.ram[i].ram < 50) {
                    document.getElementById(servername + 'c').style = "color: #66ccff;";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.ram[i].ram).options.barColor = '#66ccff';
                } else if (data.ram[i].ram < 80) {
                    document.getElementById(servername + 'c').style = "color: #ffcc66;";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.ram[i].ram).options.barColor = '#ffcc66';
                } else {
                    document.getElementById(servername + 'c').style = "color: #f00;";
                    //var $box = $('#' + servername).closest('.infobox');
                    //var barColor = 'brown';//$('#' + servername).data('color');// || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                    $('#' + servername).data('easyPieChart').update(data.ram[i].ram).options.barColor = '#f00';
                }
                document.getElementById(servername + 't').innerHTML = data.ram[i].ram + "";
                document.getElementById(servername + 'i').innerHTML = data.ram[i].raminfo + "";
            }
    //    }
    //}
    //const diskHttp = new XMLHttpRequest();
    //diskHttp.open("GET", 'info/disk');
    //diskHttp.send();
    //diskHttp.onreadystatechange = function() {
    //    if(diskHttp.readyState == 4 && diskHttp.status == 200){
    //        var data = JSON.parse(diskHttp.responseText);
            var p = "";
            for (i = 0; i < data.diskfo; i++) {
                p += data.disk[i].name + ' ' + data.disk[i].diskinfo + "<br>";
                servername = data.disk[i].name.replace('/', '_')
                servername = servername.replace('/', '_')
                servername = servername.replace('/', '_')
                servername = servername.replace('/', '_')
                servername = servername + i
                //var s = document.getElementById(servername);
                //$("#" + servername + "A").attr("data-percent", data.disk[i].disk + '%')
                //document.getElementById(servername + "B").style = "width:" + data.disk[i].disk + "%;";
                //document.getElementById(servername + "info").innerHTML = data.disk[i].diskinfo;
                if (data.disk[i].disk < 30) {
                    document.getElementById(servername + 'diskb').className = "progress-bar progress-bar-success";
                } else if (data.disk[i].disk < 50) {
                    document.getElementById(servername + 'diskb').className = "progress-bar";
                } else if (data.disk[i].disk < 80) {
                    document.getElementById(servername + 'diskb').className = "progress-bar progress-bar-warning";
                } else {
                    document.getElementById(servername + 'diskb').className = "progress-bar progress-bar-danger";
                }
                document.getElementById(servername + 'diskb').style = "width:" + data.disk[i].disk + "%;";
            }
            //document.getElementById('diskinfotext').innerHTML = p;
            for (i = 0; i < data.disksmfo; i++) {
                p += data.disksm[i].name + ' ' + data.disksm[i].diskinfo + "<br>";
                servername = data.disksm[i].name.replace('/', '_')
                servername = servername.replace('/', '_')
                servername = servername.replace('/', '_')
                servername = servername.replace('/', '_')
                servername = servername + i
                //var s = document.getElementById(servername);
                //$("#" + servername + "A").attr("data-percent", data.disk[i].disk + '%')
                //document.getElementById(servername + "B").style = "width:" + data.disk[i].disk + "%;";
                //document.getElementById(servername + "info").innerHTML = data.disk[i].diskinfo;
                if (data.disksm[i].disk < 50) {
                    document.getElementById(servername + 'diskb').className = "progress-bar progress-bar-success";
                } else if (data.disksm[i].disk < 85) {
                    document.getElementById(servername + 'diskb').className = "progress-bar";
                } else if (data.disksm[i].disk < 95) {
                    document.getElementById(servername + 'diskb').className = "progress-bar progress-bar-warning";
                } else {
                    document.getElementById(servername + 'diskb').className = "progress-bar progress-bar-danger";
                }
                document.getElementById(servername + 'diskb').style = "width:" + data.disksm[i].disk + "%;";
                document.getElementById(servername + '').innerHTML = data.disksm[i].diskinfo + "<br>";
            }
        }
    }

}

function update(){
    $('.easy-pie-chart.percentage').each(function(){
        var $box = $(this).closest('.infobox');
        var barColor = $(this).data('color') || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
        var trackColor = barColor == 'rgba(255,255,255,0.95)' ? 'rgba(255,255,255,0.25)' : '#E2E2E2';
        var size = parseInt($(this).data('size')) || 50;
        $(this).easyPieChart({
            barColor: barColor,
            trackColor: trackColor,
            scaleColor: false,
            lineCap: 'butt',
            lineWidth: parseInt(size/10),
            animate: ace.vars['old_ie'] ? false : 1000,
            size: size
        });
    });
}