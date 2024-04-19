<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta charset="utf-8" />
    <title>集群管理</title>

    <meta name="description" content="" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" />

    <!-- bootstrap & fontawesome -->
    <link rel="stylesheet" href="assets/css/bootstrap.min.css" />
    <link rel="stylesheet" href="assets/font-awesome/4.5.0/css/font-awesome.min.css" />

    <!-- page specific plugin styles -->
    <link rel="stylesheet" href="assets/css/jquery-ui.custom.min.css" />
    <link rel="stylesheet" href="assets/css/jquery.gritter.min.css" />

    <!-- text fonts -->
    <link rel="stylesheet" href="assets/css/fonts.googleapis.com.css" />

    <!-- ace styles -->
    <link rel="stylesheet" href="assets/css/ace.min.css" class="ace-main-stylesheet" id="main-ace-style" />

    <!--[if lte IE 9]>
        <link rel="stylesheet" href="assets/css/ace-part2.min.css" class="ace-main-stylesheet" />
    <![endif]-->
    <link rel="stylesheet" href="assets/css/ace-skins.min.css" />
    <link rel="stylesheet" href="assets/css/ace-rtl.min.css" />

    <!--[if lte IE 9]>
      <link rel="stylesheet" href="assets/css/ace-ie.min.css" />
    <![endif]-->
    <!-- inline styles related to this page -->
    <!-- ace settings handler -->
    <script src="assets/js/ace-extra.min.js"></script>

    <!-- HTML5shiv and Respond.js for IE8 to support HTML5 elements and media queries -->
    <!--[if lte IE 8]>
    <script src="assets/js/html5shiv.min.js"></script>
    <script src="assets/js/respond.min.js"></script>
    <![endif]-->
    <style>
        @media (min-width: 768px){
            .bankuan {
                width: 50%;
            }
        }
    </style>
</head>

<body class="no-skin">
    <div id="navbar" class="navbar navbar-default          ace-save-state">
        <div class="navbar-container ace-save-state" id="navbar-container">
            <button type="button" class="navbar-toggle menu-toggler pull-left" id="menu-toggler" data-target="#sidebar">
                <span class="sr-only">切换侧边栏</span>

                <span class="icon-bar"></span>

                <span class="icon-bar"></span>

                <span class="icon-bar"></span>
            </button>

            <div class="navbar-header pull-left">
                <a href="./" class="navbar-brand">
                    <small>
                        <i class="fa fa-leaf"></i>
                        集群管理
                    </small>
                </a>
            </div>

            <div class="navbar-buttons navbar-header pull-right" role="navigation">
                <ul class="nav ace-nav">
                    <?php include '../main/wutz.html'; ?>

                    <li class="light-blue dropdown-modal">
                        <a data-toggle="dropdown" href="#" class="dropdown-toggle">
                            <img class="nav-user-photo" src="assets/images/avatars/user.jpg" alt="Jason's Photo" />
                            <span class="user-info">
                                <small>欢迎,</small>
                                <?php echo $user; ?>
                            </span>

                            <i class="ace-icon fa fa-caret-down"></i>
                        </a>

                        <?php include '../main/usercaidan.html'; ?>
                    </li>
                </ul>
            </div>
        </div><!-- /.navbar-container -->
    </div>

    <div class="main-container ace-save-state" id="main-container">
        <script type="text/javascript">
            try { ace.settings.loadState('main-container') } catch (e) { }
        </script>

        <div id="sidebar" class="sidebar                  responsive                    ace-save-state">
            <script type="text/javascript">
                try { ace.settings.loadState('sidebar') } catch (e) { }
            </script>

            <div class="sidebar-shortcuts" id="sidebar-shortcuts">
                <div class="sidebar-shortcuts-large" id="sidebar-shortcuts-large">
                    <button class="btn btn-success">
                        <i class="ace-icon fa fa-signal"></i>
                    </button>

                    <button class="btn btn-info">
                        <i class="ace-icon fa fa-pencil"></i>
                    </button>

                    <button class="btn btn-warning">
                        <i class="ace-icon fa fa-users"></i>
                    </button>

                    <button class="btn btn-danger" onclink="location.href='./setup?link=127.0.0.1'" tybe="button">
                        <i class="ace-icon fa fa-cogs"></i>
                    </button>
                </div>

                <div class="sidebar-shortcuts-mini" id="sidebar-shortcuts-mini">
                    <span class="btn btn-success"></span>

                    <span class="btn btn-info"></span>

                    <span class="btn btn-warning"></span>

                    <span onclick="javascript:window.open('./setup?link=127.0.0.1')" class="btn btn-danger"></span>
                </div>
            </div><!-- /.sidebar-shortcuts -->

            <ul class="nav nav-list" id="biao">
                <li class="">
                    <a href="">
                        <span class="menu-text">正在加载</span>
                    </a>
                    <b class="arrow"></b>
                </li>
            </ul><!-- /.nav-list -->



            <div class="sidebar-toggle sidebar-collapse" id="sidebar-collapse">
                <i id="sidebar-toggle-icon" class="ace-icon fa fa-angle-double-left ace-save-state" data-icon1="ace-icon fa fa-angle-double-left" data-icon2="ace-icon fa fa-angle-double-right"></i>
            </div>
        </div>

        <div class="main-content">
            <div class="main-content-inner">
                <div class="breadcrumbs ace-save-state" id="breadcrumbs">
                    <ul class="breadcrumb">
                        <li class="active">集群管理</li>
                    </ul><!-- /.breadcrumb -->

                    <div class="nav-search" id="nav-search">
                        <form class="form-search">
                            <span class="input-icon">
                                <input type="text" placeholder="Search ..." class="nav-search-input" id="nav-search-input" autocomplete="off" />
                                <i class="ace-icon fa fa-search nav-search-icon"></i>
                            </span>
                        </form>
                    </div><!-- /.nav-search -->
                </div>

                <div class="page-content">
                    <?php include '../main/ace-settings-container.html'; ?>

                    <div class="row" id="row">
                        <div class="tabbable">
					        <ul class="nav nav-tabs" id="myTab">

								<!--li>
									<a data-toggle="tab" href="#messages">
										Messages
										<span class="badge badge-danger">4</span>
									</a>
								</li-->

								<li class="active">				            
                                    <a data-toggle="tab" href="#tab1n" id="tab1" aria-expanded="true">					            
                                        <i class="green ace-icon fa fa-home bigger-120"></i>					            
                                        QEMU 				            
                                    </a>			            
                                </li>
                            </ul>

							<div class="tab-content" style="height: 100%;" id="tabn">
                                    
								<div id="tab1n" class="tab-pane fade active in">
                                        <!-- PAGE CONTENT BEGINS -->
                                        <div class="table-header">
                                            <div class="widget-toolbar" style="float:none;position: static;">QEMU</div>
                                            
                                            <!--a href="#my-modal" role="button" class="pull-right green" data-toggle="modal"-->
                                            <div class="widget-toolbar" style="float:none;">
                                                    CPU: &ensp;<div class="progress progress-mini progress-striped active pos-rel" style="width:60px;background:#abbac3;" data-percent="-1%" id="hostcpu">
                                                        <div class="progress-bar progress-bar-danger" style="width:1%" id="hostcpub"></div>
                                                    </div>
                                                </div>
                                                <div class="widget-toolbar" style="float:none;">
                                                    RAM: &ensp;<div class="progress progress-mini progress-striped active pos-rel" style="width:60px;background:#abbac3;" data-percent="-1%" id="hostram">
                                                        <div class="progress-bar progress-bar-danger" style="width:1%" id="hostramb"></div>
                                                    </div>
                                                </div>
                                                <div class="widget-toolbar" style="float:none;">
                                                    IO: &ensp;<div class="progress progress-mini progress-striped active pos-rel" style="width:60px;background:#abbac3;" data-percent="-1%" id="hostio">
                                                        <div class="progress-bar progress-bar-danger" style="width:1%" id="hostiob"></div>
                                                    </div>
                                                </div>

                                                <div class="widget-toolbar">
                                                    <button id="bootbox-options" class="btn btn-xs bigger btn-danger" data-toggle="modal"  onclick="up_biao();">
                                                        <!--i class="ace-icon fa fa-times"></i-->
                                                        刷新
                                                    </button>
                                                    
                                                    <button id="bootbox-options" class="btn btn-xs bigger btn-success " data-toggle="modal" data-target="#my-modal"  onclick='add();'>
                                                        <!--i class="ace-icon fa fa-times"></i-->
                                                        添加
                                                    </button>
                                                </div>
                                                
                                            <!--/a-->
                                        </div>
                                        <!-- PAGE CONTENT BEGINS -->
                                        <div class="row">
                                            <div class="col-xs-12">
                                                <table id="simple-table" class="table  table-bordered table-hover">
                                                    <thead id="biaotou">
                                                        <tr>
                                                            <th class="detail-col">
                                                                <label class="pos-rel">
                                                                    <input type="checkbox" class="ace" />
                                                                    <span class="lbl"></span>
                                                                </label>
                                                            </th>
                                                            <th class="hidden-480">名称</th>
                                                            <th class="detail-col">状态</th>
                                                            <th class="hidden-480">CPU</th>
                                                            <th class="hidden-480">内存</th>
                                                            <th class="hidden-480" style="width: 205px">操作</th>
                                                        </tr>
                                                    </thead>

                                                    <tbody id="biaoinfo">
                                                        

                                                    </tbody>

                                                </table>
                                            </div><!-- /.span -->
                                        </div><!-- /.row -->		            
                                </div>
								
								<div id="editqemu" class="tab-pane fade in">				            
                                    <a id="edittab" data-toggle="tab" href="#editqemu" class="fade">add</a>
                                        <!-- PAGE CONTENT BEGINS -->
                                        <div class="table-header">
                                            编辑
                                                <button id="bootbox-options" class="pull-right btn btn-sm btn-success " data-toggle="modal" data-target="#my-modal"  onclick='add();'>
                                                    <!--i class="ace-icon fa fa-times"></i-->
                                                    添加
                                                </button>
                                            <!--/a-->
                                        </div>
                                        <!-- PAGE CONTENT BEGINS -->
                                        <div class="row">
                                            <div class="col-xs-12">
                                                <table id="simple-table" class="table  table-bordered table-hover">
                                                    <thead id="biaotou">
                                                        <tr>
                                                            <th class="detail-col">
                                                                <label class="pos-rel">
                                                                    <input type="checkbox" class="ace" />
                                                                    <span class="lbl"></span>
                                                                </label>
                                                            </th>
                                                            <th class="hidden-480">名称</th>
                                                            <th class="detail-col">状态</th>
                                                            <th class="hidden-480">CPU</th>
                                                            <th class="hidden-480">内存</th>
                                                            <th class="hidden-480" style="width: 205px">操作</th>
                                                        </tr>
                                                    </thead>

                                                    <tbody id="biaoinfo">
                                                        

                                                    </tbody>

                                                </table>
                                            </div><!-- /.span -->
                                        </div><!-- /.row -->	
                                </div>
                            </div>
							</div>
                            <div id="my-modal" class="modal fade" tabindex="-1" data-backdrop=false >
                                <div class="modal-dialog" style="">
                                    <div class="modal-content" >
                                        <div class="modal-header">
                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true" onclick="up_biao()">&times;</button>
                                            <h3 class="smaller lighter blue no-margin"><div id="h3text">正在加载</div></h3>
                                        </div>

                                        <div class="modal-body" id="adddiv">
                                            <div class="row">
                                                <div class="col-xs-12">
                                                    <table id="simple-table" class="table  table-bordered table-hover">
                                                        <thead id="biaotou">
                                                            <tr>
                                                                <th class="detail-col">名称</th>
                                                                <th class="hidden-480">值</th>
                                                            </tr>
                                                        </thead>

                                                        <tbody id="biaoinfo">
                                                            <tr>
                                                                <th class="detail-col">名称</th>
                                                                <th class="hidden-480">
                                                                    <input type="text" id="qemu_name" class="form-control" placeholder="名称" onblur="up_addqemu_dir()">
                                                                </th>
                                                            </tr>
                                                            <tr>
                                                                <th class="detail-col">目录</th>
                                                                <th class="hidden-480">
                                                                    <input type="text" id="qemu_dir" class="form-control" placeholder="虚拟机存放目录" value="/root/qemu/">
                                                                </th>
                                                            </tr>
                                                            <tr>
                                                                <th class="detail-col">SMP</th>
                                                                <th class="hidden-480">
                                                                    <input type="text" id="qemu_smp" class="form-control" placeholder="核心">
                                                                </th>
                                                            </tr>
                                                            <tr>
                                                                <th class="detail-col">RAM</th>
                                                                <th class="hidden-480">
                                                                    <input type="text" id="qemu_ram" class="form-control" placeholder="内存">
                                                                </th>
                                                            </tr>
                                                            <tr>
                                                                <th class="detail-col">Disk</th>
                                                                <th class="hidden-480">
                                                                    <input type="text" id="qemu_disk" class="form-control" placeholder="硬盘大小">
                                                                </th>
                                                            </tr>

                                                        </tbody>

                                                    </table>
                                                </div><!-- /.span -->
                                            </div><!-- /.row -->	

                                        <div class="modal-footer">
                                            <button class="btn btn-sm btn-success pull-right" data-dismiss="modal" onclick="addpost()">
                                                <i class="ace-icon fa fa-check"></i>
                                                确认
                                            </button>
                                            <button class="btn btn-sm btn-danger pull-right" data-dismiss="modal" onclick="up_biao()">
                                                <i class="ace-icon fa fa-times"></i>
                                                取消
                                            </button>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div>
                    </div><!-- /.row -->
                </div><!-- /.page-content -->
            </div>
        </div><!-- /.main-content -->

        <div class="footer">
            <div class="footer-inner">
                <div class="footer-content">
                    <span class="bigger-120">
                        <span class="blue bolder">Ace</span>
                        Application &copy; 2013-9014
                    </span>

                    &nbsp; &nbsp;
                    <span class="action-buttons">
                        <a href="#">
                            <i class="ace-icon fa fa-twitter-square light-blue bigger-150"></i>
                        </a>

                        <a href="#">
                            <i class="ace-icon fa fa-facebook-square text-primary bigger-150"></i>
                        </a>

                        <a href="#">
                            <i class="ace-icon fa fa-rss-square orange bigger-150"></i>
                        </a>
                    </span>
                </div>
            </div>
        </div>

        <a href="#" id="btn-scroll-up" class="btn-scroll-up btn btn-sm btn-inverse">
            <i class="ace-icon fa fa-angle-double-up icon-only bigger-110"></i>
        </a>
    </div><!-- /.main-container -->
    <!-- basic scripts -->
    <!--[if !IE]> -->
    <script src="assets/js/jquery-2.1.4.min.js"></script>

    <!-- <![endif]-->
    <!--[if IE]>
    <script src="assets/js/jquery-1.11.3.min.js"></script>
    <![endif]-->
    <script type="text/javascript">
        if ('ontouchstart' in document.documentElement) document.write("<script src='assets/js/jquery.mobile.custom.min.js'>" + "<" + "/script>");
    </script>

    <script src="assets/js/bootstrap.min.js"></script>
    <script src="assets/js/jquery.dataTables.min.js"></script>
    <script src="assets/js/jquery.dataTables.bootstrap.min.js"></script>
    <script src="assets/js/dataTables.buttons.min.js"></script>
    <script src="assets/js/buttons.flash.min.js"></script>
    <script src="assets/js/buttons.html5.min.js"></script>
    <script src="assets/js/buttons.print.min.js"></script>
    <script src="assets/js/buttons.colVis.min.js"></script>
    <script src="assets/js/dataTables.select.min.js"></script>

    <script src="assets/js/wizard.min.js"></script>
    <script src="assets/js/jquery.validate.min.js"></script>
    <script src="assets/js/jquery-additional-methods.min.js"></script>
    <script src="assets/js/bootbox.js"></script>
    <script src="assets/js/jquery.maskedinput.min.js"></script>
    <script src="assets/js/select2.min.js"></script>
    <script src="assets/js/jquery-ui.custom.min.js"></script>
    <script src="assets/js/jquery.ui.touch-punch.min.js"></script>
    <!-- page specific plugin scripts -->
    <script src="assets/js/jquery.easypiechart.min.js"></script>
    <!-- ace scripts -->
    <script src="assets/js/ace-elements.min.js"></script>
    <script src="assets/js/ace.min.js"></script>
    <!--script src="APP/index.js"></script-->
    <script src="index.js"></script>
    <script type="text/javascript">
        jQuery(function ($) {
            /////////////////////////////////
            
        })
        
    </script>
    <script type="text/javascript">
        window.onload = function () {
            //userinit();
            //up_biao();
            var hei = window.innerHeight;
            if(hei > 250){
                //document.getElementById('tab3n').style.height = hei - 250 + 'px';
            }
            
            up_biao();
            window.setInterval(up_biao, 1000);
        }
        function stop_qemu(name){
            bootbox.confirm("确认关闭虚拟机 " + name, function (result) {
                if(result){
                    var reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
                    var r = window.location.search.substr(1).match(reg);
                    if (r == null){
                        r = ['127.0.0.1','127.0.0.1','127.0.0.1'];
                    }
                    const Http = new XMLHttpRequest();
                    var rul = catrul("qemu/api?");
                    Http.open("GET",rul + '&type=stop' + '&name=' + name);
                    Http.send();
                    Http.onreadystatechange = (e) => {
                        if(Http.readyState == 4 && Http.status == 200){
                            if (Http.status == 200) {
                                cathttp = Http.responseText;
                                if (cathttp.substr(0, 1) == "<") {
                                    location.reload();
                                } else {
                                    var data = JSON.parse(cathttp); 
                                        
                                        bootbox.confirm(data.data, function (result) {

                                        })
                                    up_biao();
                                }
                            }
                        }
                    }
                }
            })
        }
        function kill_qemu(name){
            bootbox.confirm("确认杀死虚拟机 " + name, function (result) {
                if(result){
                    var reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
                    var r = window.location.search.substr(1).match(reg);
                    if (r == null){
                        r = ['127.0.0.1','127.0.0.1','127.0.0.1'];
                    }
                    const Http = new XMLHttpRequest();
                    var rul = catrul("qemu/api?");
                    Http.open("GET",rul + '&type=kill' + '&name=' + name);
                    Http.send();
                    Http.onreadystatechange = (e) => {
                        if(Http.readyState == 4 && Http.status == 200){
                            if (Http.status == 200) {
                                cathttp = Http.responseText;
                                if (cathttp.substr(0, 1) == "<") {
                                    location.reload();
                                } else {
                                    var data = JSON.parse(cathttp); 
                                        
                                        bootbox.confirm(data.data, function (result) {

                                        })
                                    up_biao();
                                }
                            }
                        }
                    }
                }
            })
        }
        function up_addqemu_dir(){
            qemu_name = document.getElementById('qemu_name').value;
            document.getElementById('qemu_dir').value = "/root/qemu/" + qemu_name;
        }
        function addpost(){
            var reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
            var r = window.location.search.substr(1).match(reg);
            if (r == null){
                r = ['127.0.0.1','127.0.0.1','127.0.0.1'];
            }
            //edit = document.getElementById('h3text').innerHTML;
            qemu_name = document.getElementById('qemu_name').value;
            qemu_dir  = document.getElementById('qemu_dir').value;
            qemu_smp  = document.getElementById('qemu_smp').value;
            qemu_ram  = document.getElementById('qemu_ram').value;
            qemu_disk  = document.getElementById('qemu_disk').value;

            const Http = new XMLHttpRequest();
            var rul = catrul("qemu/api?");
            Http.open("GET",rul + 
            '&qemu_name=' + qemu_name + 
            '&qemu_dir=' + qemu_dir + 
            '&qemu_smp=' + qemu_smp + 
            '&qemu_ram=' + qemu_ram + 
            '&qemu_disk=' + qemu_disk + 
            '&type=' + "addpost");
            Http.send();
            Http.onreadystatechange = (e) => {
                if(Http.readyState == 4 && Http.status == 200){
                    if (Http.status == 200) {
                        cathttp = Http.responseText;
                        if (cathttp.substr(0, 1) == "<") {
                            location.reload();
                        } else {
                                var data = JSON.parse(cathttp); 
                                if (data.data == 'ERROR'){
                                    var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=com";
                                    bootbox.confirm(data.data + '<iframe src="' + rul + '" width="100%" height="100%"></iframe>	', function (result) {

                                    })
                                }else{
                                    
                                    bootbox.confirm(data.data, function (result) {

                                    })
                                }
                                up_biao();
                            }
                    }
                }
            }
        }
        function edit(name){
            document.getElementById('edittab').click();

            document.getElementById('name').disabled  = true;
            document.getElementById('name').value  = name;
            document.getElementById('id').value  = name;
            document.getElementById('type').disabled  = true;
            document.getElementById('local_ip').disabled  = true;
            document.getElementById('local_port').disabled  = true;
            document.getElementById('remote_port').disabled  = true;
            var reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
            var r = window.location.search.substr(1).match(reg);
            if (r == null){
                r = ['127.0.0.1','127.0.0.1','127.0.0.1'];
            }
            const Http = new XMLHttpRequest();
            var rul = catrul("frpc/api?");
            Http.open("GET",rul + '&type=run');
            Http.send();
            Http.onreadystatechange = (e) => {
                if(Http.readyState == 4 && Http.status == 200){
                    if (Http.status == 200) {
                        cathttp = Http.responseText;
                        if (cathttp.substr(0, 1) == "<") {
                            location.reload();
                        } else {
                            var data = JSON.parse(cathttp);
                            var reg = "";
                            var link = "";
                            for (i = 0; i < data.datafo; i++) {
                                if (data.data[i].name == document.getElementById('name').value){
                                    document.getElementById('h3text').innerHTML  = "edit";
                                    document.getElementById('name').value  = data.data[i].name;
                                    document.getElementById('type').value  = data.data[i].type;;
                                    document.getElementById('local_ip').value  = data.data[i].local_ip;;
                                    document.getElementById('local_port').value  = data.data[i].local_port;;
                                    document.getElementById('remote_port').value  = data.data[i].remote_port;;
                                    document.getElementById('name').disabled  = false;
                                    document.getElementById('type').disabled  = false;
                                    document.getElementById('local_ip').disabled  = false;
                                    document.getElementById('local_port').disabled  = false;
                                    document.getElementById('remote_port').disabled  = false;
                                }
                            }
                        }
                    }
                }
            }
        }
        function up_post(data){
            if (data == "start"){
                document.getElementById('start').disabled  = true;
                const Http = new XMLHttpRequest();
                var rul = catrul("qemu/api?");
                Http.open("GET",rul + '&type=start');
                Http.send();
                Http.onreadystatechange = (e) => {
                    if(Http.readyState == 4 && Http.status == 200){
                        document.getElementById('start').disabled  = false;
                        if (Http.status == 200) {
                            cathttp = Http.responseText;
                            if (cathttp.substr(0, 1) == "<") {
                                location.reload();
                            } else {
                                var data = JSON.parse(cathttp); 
                                if (data.data == 'ERROR'){
                                    var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
                                    bootbox.confirm(data.data + '<iframe src="' + rul + '" width="100%" height="100%"></iframe>	', function (result) {

                                    })
                                }else{
                                    
                                    bootbox.confirm(data.data, function (result) {

                                    })
                                }
                                up_biao();
                                var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
                                document.getElementById('logs').src = rul;
                            }
                        }
                    }
                }
            }else if (data == "stop"){
                document.getElementById('start').disabled  = true;
                const Http = new XMLHttpRequest();
                var rul = catrul("frpc/api?");
                Http.open("GET",rul + '&type=stop');
                Http.send();
                Http.onreadystatechange = (e) => {
                    if(Http.readyState == 4 && Http.status == 200){
                        document.getElementById('start').disabled  = false;
                        if (Http.status == 200) {
                            cathttp = Http.responseText;
                            if (cathttp.substr(0, 1) == "<") {
                                location.reload();
                            } else {
                                var data = JSON.parse(cathttp); 
                                if (data.data == 'ERROR'){
                                    var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
                                    bootbox.confirm(data.data + '<iframe src="' + rul + '" width="100%" height="100%"></iframe>	', function (result) {

                                    })
                                }else{
                                    
                                    bootbox.confirm(data.data, function (result) {

                                    })
                                }
                                up_biao();
                                var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
                                document.getElementById('logs').src = rul;
                            }
                        }
                    }
                }
            }else if (data == "booton"){
                //document.getElementById('start').disabled  = true;
                const Http = new XMLHttpRequest();
                var rul = catrul("frpc/api?");
                Http.open("GET",rul + '&type=booton');
                Http.send();
                Http.onreadystatechange = (e) => {
                    if(Http.readyState == 4 && Http.status == 200){
                        //document.getElementById('start').disabled  = false;
                        if (Http.status == 200) {
                            cathttp = Http.responseText;
                            if (cathttp.substr(0, 1) == "<") {
                                location.reload();
                            } else {
                                var data = JSON.parse(cathttp); 
                                if (data.data == 'ERROR'){
                                    var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
                                    bootbox.confirm(data.data + '<iframe src="' + rul + '" width="100%" height="100%"></iframe>	', function (result) {

                                    })
                                }else{
                                    
                                    bootbox.confirm(data.data, function (result) {

                                    })
                                }
                                up_biao();
                                var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
                                document.getElementById('logs').src = rul;
                            }
                        }
                    }
                }
            }else if (data == "bootoff"){
                //document.getElementById('start').disabled  = true;
                const Http = new XMLHttpRequest();
                var rul = catrul("frpc/api?");
                Http.open("GET",rul + '&type=bootoff');
                Http.send();
                Http.onreadystatechange = (e) => {
                    if(Http.readyState == 4 && Http.status == 200){
                        //document.getElementById('start').disabled  = false;
                        if (Http.status == 200) {
                            cathttp = Http.responseText;
                            if (cathttp.substr(0, 1) == "<") {
                                location.reload();
                            } else {
                                var data = JSON.parse(cathttp); 
                                if (data.data == 'ERROR'){
                                    var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
                                    bootbox.confirm(data.data + '<iframe src="' + rul + '" width="100%" height="100%"></iframe>	', function (result) {

                                    })
                                }else{
                                    
                                    bootbox.confirm(data.data, function (result) {

                                    })
                                }
                                up_biao();
                                var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
                                document.getElementById('logs').src = rul;
                            }
                        }
                    }
                }
            }else if (data == "server"){
                //document.getElementById('start').disabled  = true;
                const Http = new XMLHttpRequest();
                var rul = catrul("qemu/api?");
                server = document.getElementById('server').value;
                port = document.getElementById('port').value;
                token = document.getElementById('token').value;
                Http.open("GET",rul + '&type=server&server=' + server + "&port=" + port + "&tocken=" + token);
                Http.send();
                Http.onreadystatechange = (e) => {
                    if(Http.readyState == 4 && Http.status == 200){
                        //document.getElementById('start').disabled  = false;
                        if (Http.status == 200) {
                            cathttp = Http.responseText;
                            if (cathttp.substr(0, 1) == "<") {
                                location.reload();
                            } else {
                                var data = JSON.parse(cathttp); 
                                if (data.data == 'ERROR'){
                                    var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=com";
                                    bootbox.confirm(data.data + '<iframe src="' + rul + '" width="100%" height="100%"></iframe>	', function (result) {

                                    })
                                }else{
                                    
                                    bootbox.confirm(data.data, function (result) {

                                    })
                                }
                                up_biao();
                                var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
                                document.getElementById('logs').src = rul;
                            }
                        }
                    }
                }
            }else if (data == "web"){
                //document.getElementById('start').disabled  = true;
                const Http = new XMLHttpRequest();
                var rul = catrul("qemu/api?");
                admin_addr = document.getElementById('admin_addr').value;
                admin_port = document.getElementById('admin_port').value;
                admin_user = document.getElementById('admin_user').value;
                admin_pwd = document.getElementById('admin_pwd').value;
                Http.open("GET",rul + '&type=web&admin_addr=' + admin_addr + "&admin_port=" + admin_port + "&admin_user=" + admin_user + "&admin_pwd=" + admin_pwd);
                Http.send();
                Http.onreadystatechange = (e) => {
                    if(Http.readyState == 4 && Http.status == 200){
                        //document.getElementById('start').disabled  = false;
                        if (Http.status == 200) {
                            cathttp = Http.responseText;
                            if (cathttp.substr(0, 1) == "<") {
                                location.reload();
                            } else {
                                var data = JSON.parse(cathttp); 
                                if (data.data == 'ERROR'){
                                    var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=com";
                                    bootbox.confirm(data.data + '<iframe src="' + rul + '" width="100%" height="100%"></iframe>	', function (result) {

                                    })
                                }else{
                                    
                                    bootbox.confirm(data.data, function (result) {

                                    })
                                }
                                up_biao();
                                var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
                                document.getElementById('logs').src = rul;
                            }
                        }
                    }
                }
            }else{
                bootbox.confirm('没写 data: ' + data, function (result) {
                    
                })
            }
        }
        function start_qemu(data){
            var reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
            var r = window.location.search.substr(1).match(reg);
            if (r == null){
                r = ['127.0.0.1','127.0.0.1','127.0.0.1'];
            }
            const Http = new XMLHttpRequest();
            var rul = catrul("qemu/api?");
            Http.open("GET",rul + '&type=start&name=' + data);
            Http.send();
            Http.onreadystatechange = (e) => {
                if(Http.readyState == 4 && Http.status == 200){
                    cathttp = Http.responseText;
                    var data = JSON.parse(cathttp); 
                    bootbox.confirm(data.data, function (result) {
                        if(result){
                            if(data.data == "Start"){
                                window.open('/vnc/?path=websockify?token=' + data.soket + '&autoconnect=1&resize=browser','_blank','toolbar=no,location=no,status=no,menubar=no,resizable=yes,width=800,height=420');
                            }
                        }
                    })
                }
            }
        }
        
        function up_biao() {
            var reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
            var r = window.location.search.substr(1).match(reg);
            if (r == null){
                r = ['127.0.0.1','127.0.0.1','127.0.0.1'];
            }
            const Http = new XMLHttpRequest();
            var rul = catrul("qemu/api?");
            Http.open("GET",rul + '&type=run');
            Http.send();
            Http.onreadystatechange = (e) => {
                if(Http.readyState == 4 && Http.status == 200){
                    if (Http.status == 200) {
                        cathttp = Http.responseText;
                        if (cathttp.substr(0, 1) == "<") {
                            location.reload();
                        } else {
                            var data = JSON.parse(cathttp);
                            
                            $("#hostcpu").attr("data-percent", data.cpu + "%")
                            jdtb = document.getElementById("hostcpub");
                            jdtb.style = "width:" + data.cpu + "%;";
                            $("#hostram").attr("data-percent", data.ram + "%")
                            jdtb = document.getElementById("hostramb");
                            jdtb.style = "width:" + data.ram + "%;";
                            $("#hostio").attr("data-percent", data.io + "%")
                            jdtb = document.getElementById("hostiob");
                            jdtb.style = "width:" + data.io + "%;";

                            var reg = "";
                            var link = "";
                            for (i = 0; i < data.fo; i++) {
                                servername = data.data[i].name
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                servername = servername.replace('.', '_')
                                reg = reg + '<tr>';
                                reg = reg + '<td class="center">';
                                reg = reg + '<label class="pos-rel">';
                                reg = reg + '<input type="checkbox" class="ace" />';
                                reg = reg + '<span class="lbl"></span>';
                                reg = reg + '</label>';
                                reg = reg + '</td>';
                                reg = reg + '<td>';
                                reg = reg + '<a href="' + data.data[i].name + '">' + data.data[i].name + '</a>';
                                reg = reg + '</td>';
                                reg = reg + '<td id="' + servername + "info" + '">';
                                if (data.data[i].api == "0") { reg = reg + '<span class="label label-sm label-warning">未找到</span>' }
                                if (data.data[i].api == "1") { reg = reg + '<span class="label label-sm label-danger">关机</span>' }
                                if (data.data[i].api == "2") { reg = reg + '<span class="label label-sm label-success">开机</span>' }
                                if (data.data[i].api == "3") { reg = reg + '<span class="label label-sm label-inverse">不知道</span>' }
                                reg = reg + '</td>';
                                reg = reg + '<td id="' + servername + "info" + '">';
                                reg = reg + '<div class="progress pos-rel" data-percent="' + data.data[i].cpu + '%" id="' + servername + "cpua" + '">';
                                reg = reg + '<div class="progress-bar" style="width:' + data.data[i].cpu + '%;" id="' + servername + "cpub" + '"></div>';
                                reg = reg + '</div>'
                                reg = reg + '</td>';
                                reg = reg + '<td id="' + servername + "info" + '">';
                                reg = reg + '<div class="progress pos-rel" data-percent="' + data.data[i].ram + '%" id="' + servername + "cpua" + '">';
                                reg = reg + '<div class="progress-bar" style="width:' + data.data[i].ram + '%;" id="' + servername + "cpub" + '"></div>';
                                reg = reg + '</div>'
                                reg = reg + '</td>';
                                reg = reg + '<td><div class="hidden-sm btn-group">';
                                if (data.data[i].api == "1"){
                                    reg = reg + '<button class="btn btn-sm btn-success" data-toggle="modal" onclick="start_qemu(\'' + data.data[i].name + '\');">\
                                                    <!--i class="ace-icon fa fa-download bigger-120"></i-->开机\
                                                    </button>';
                                }
                                if (data.data[i].api == "2"){
                                    reg = reg + '<button class="btn btn-sm btn-danger" data-toggle="modal" onclick="stop_qemu(\'' + data.data[i].name + '\');">\
                                                    <!--i class="ace-icon fa fa-download bigger-120"></i-->关机\
                                                    </button>';
                                    reg = reg + '<button class="btn btn-sm btn-danger" data-toggle="modal" onclick="kill_qemu(\'' + data.data[i].name + '\');">\
                                                    <!--i class="ace-icon fa fa-download bigger-120"></i-->kill\
                                                    </button>';
                                }
                                reg = reg + '\
                                                <button class="btn btn-sm btn-success" data-toggle="modal" onclick="window.open(\'/vnc/?path=websockify?token=' + data.data[i].soket + '&autoconnect=1&resize=browser\',\'_blank\',\'toolbar=no,location=no,status=no,menubar=no,resizable=yes,width=800,height=420\');">\
                                                    <!--i class="ace-icon fa fa-download bigger-120"></i-->VNC\
                                                </button>';
                                reg = reg + '\
                                                <button class="btn btn-sm btn-success" data-toggle="modal" onclick="edit(\'' + data.data[i].name + '\');">\
                                                    <!--i class="ace-icon fa fa-download bigger-120"></i-->编辑\
                                                </button>\
                                        </td >';
                                reg = reg + '</div></tr>';
                                reg = reg + '';
                            }
                            document.getElementById("biaoinfo").innerHTML = reg;
                        }
                    }
                }
            }
        }
    </script>

    <!-- inline scripts related to this page -->
    
</body>
</html>
