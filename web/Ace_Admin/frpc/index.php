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
                                        frp 				            
                                    </a>			            
                                </li>
								<li class="">				            
                                    <a data-toggle="tab" href="#tab2n" id="tab2" aria-expanded="true">					            
                                        <i class="green ace-icon fa fa-cog bigger-120"></i>					            
                                        设置				            
                                    </a>			            
                                </li>
								<li class="">				            
                                    <a data-toggle="tab" href="#tab3n" id="tab3" aria-expanded="true">					            
                                        <i class="green ace-icon fa fa-cog bigger-120"></i>					            
                                        Log				            
                                    </a>			            
                                </li>
                            </ul>

							<div class="tab-content" style="height: 100%;" id="tabn">
                                    
								<div id="tab1n" class="tab-pane fade active in">
                                        <!-- PAGE CONTENT BEGINS -->
                                        <div class="table-header">
                                            FRPC
                                            <!--a href="#my-modal" role="button" class="pull-right green" data-toggle="modal"-->
                                                <button id="bootbox-options" class="pull-right btn btn-sm btn-danger" data-toggle="modal"  onclick="up_biao();">
                                                    <!--i class="ace-icon fa fa-times"></i-->
                                                    刷新
                                                </button>
                                                
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
                                                            <th class="hidden-480">链接</th>
                                                            <th class="hidden-480">端口</th>
                                                            <th class="hidden-480">状态</th>
                                                            <th class="hidden-480">操作</th>
                                                        </tr>
                                                    </thead>

                                                    <tbody id="biaoinfo">
                                                        

                                                    </tbody>

                                                </table>
                                            </div><!-- /.span -->
                                        </div><!-- /.row -->		            
                                </div>
								<div id="tab2n" class="tab-pane fade in">				            
                                    <p>
                                    <button id="start" class="btn ">正在加载</button>
                                    <button id="boot" class="btn ">正在加载</button>
                                    </p>		
                                    <p>		
                                        <div class="row">
                                        <div class="bankuan widget-container-col ui-sortable" id="widget-container-col-1" style="float: left;">
                                            <div class="widget-box ui-sortable-handle" id="widget-box-1">
                                                <div class="widget-header">
                                                    <h5 class="widget-title">基本设置</h5>

                                                    <div class="widget-toolbar">
                                                        
                                                        <a href="#" data-action="collapse">
                                                            <i class="ace-icon fa fa-chevron-up"></i>
                                                        </a>

                                                    </div>
                                                </div>

                                                <div class="widget-body">
                                                    <div class="widget-main">
                                                        
                                                        <label class="block clearfix">
                                                            <span class="block input-icon input-icon-right">
                                                                server <input type="text" id="server" class="" placeholder="服务器地址,如127.0.0.1">
                                                            </span>
                                                        </label> 
                                                        <label class="block clearfix">
                                                            <span class="block input-icon input-icon-right">
                                                                port <input type="text" id="port" class="" placeholder="服务器端口,如7000">
                                                            </span>
                                                        </label>   
                                                        <label class="block clearfix">
                                                            <span class="block input-icon input-icon-right">
                                                                token <input type="text" id="token" class="" placeholder="服务器端设置的token">
                                                            </span>
                                                        </label>   
                                                    </div>
                                                    
                                                    <div class="widget-toolbox padding-8 clearfix">
                                                        <button class="btn btn-xs btn-danger pull-left" onclick='get_post("server");return false;'>
                                                            <i class="ace-icon fa fa-times"></i>
                                                            <span class="bigger-110">还原</span>
                                                        </button>

                                                        <button class="btn btn-xs btn-success pull-right" onclick='up_post("server");return false;'>
                                                            <span class="bigger-110">保存</span>

                                                            <i class="ace-icon fa fa-arrow-right icon-on-right"></i>
                                                        </button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>  
                                        <div class="bankuan widget-container-col ui-sortable" id="widget-container-col-1" style="float: left;">
                                            <div class="widget-box ui-sortable-handle" id="widget-box-1">
                                                <div class="widget-header">
                                                    <h5 class="widget-title">web后台</h5>

                                                    <div class="widget-toolbar">
                                                        
                                                        <a href="#" data-action="collapse">
                                                            <i class="ace-icon fa fa-chevron-up"></i>
                                                        </a>

                                                    </div>
                                                </div>

                                                <div class="widget-body">
                                                    <div class="widget-main">
                                                        
                                                        <label class="block clearfix">
                                                            <span class="block input-icon input-icon-right">
                                                            admin_addr <input type="text" id="admin_addr" class="" placeholder="授权链接地址,如0.0.0.0">
                                                            </span>
                                                        </label> 
                                                        <label class="block clearfix">
                                                            <span class="block input-icon input-icon-right">
                                                            admin_port <input type="text" id="admin_port" class="" placeholder="web页面端口,如7500">
                                                            </span>
                                                        </label>   
                                                        <label class="block clearfix">
                                                            <span class="block input-icon input-icon-right">
                                                            admin_user <input type="text" id="admin_user" class="" placeholder="web页面用户,如 admin">
                                                            </span>
                                                        </label> 
                                                        <label class="block clearfix">
                                                            <span class="block input-icon input-icon-right">
                                                            admin_pwd <input type="text" id="admin_pwd" class="" placeholder="web页面密码,如 admin">
                                                            </span>
                                                        </label>   
                                                    </div>
                                                    
                                                    <div class="widget-toolbox padding-8 clearfix">
                                                        <button class="btn btn-xs btn-danger pull-left" onclick='get_post("web");return false;'>
                                                            <i class="ace-icon fa fa-times"></i>
                                                            <span class="bigger-110">还原</span>
                                                        </button>

                                                        <button class="btn btn-xs btn-success pull-right" onclick='up_post("web");return false;'>
                                                            <span class="bigger-110">保存</span>

                                                            <i class="ace-icon fa fa-arrow-right icon-on-right"></i>
                                                        </button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>  </div>
                                        
                                    </p>	      
                                </div>
								<div id="tab3n" class="tab-pane fade in">				            
                                <iframe id="logs" src="" width="100%" height="100%"></iframe>         
                                </div>
								<div id="tab4n" class="tab-pane fade in">				            
                                       
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
                                            <input id="id" name="id" type="hidden" value="4"  maxlength="" placeholder=""> 
                                            <label class="block clearfix">
                                                <span class="block input-icon input-icon-right">
                                                name <input type="text" id="name" class="" placeholder="名称">
                                                </span>
                                            </label> 
                                            <label class="block clearfix">
                                                <span class="block input-icon input-icon-right">
                                                type <input type="text" id="type" class="" placeholder="tcp,udp">
                                                </span>
                                            </label> 
                                            <label class="block clearfix">
                                                <span class="block input-icon input-icon-right">
                                                local_ip <input type="text" id="local_ip" class="" placeholder="本地服务器地址,如127.0.0.1">
                                                </span>
                                            </label> 
                                            <label class="block clearfix">
                                                <span class="block input-icon input-icon-right">
                                                local_port <input type="text" id="local_port" class="" placeholder="本地服务器端口,如8888">
                                                </span>
                                            </label>   
                                            <label class="block clearfix">
                                                <span class="block input-icon input-icon-right">
                                                remote_port <input type="text" id="remote_port" class="" placeholder="远程开放端口,如6000">
                                                </span>
                                            </label>  
                                        </div>

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
            up_biao();
            var hei = window.innerHeight;
            if(hei > 250){
                document.getElementById('tab3n').style.height = hei - 250 + 'px';
            }
            var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
            document.getElementById('logs').src = rul;
            
        }
        function add(){
            document.getElementById('h3text').innerHTML  = "add";
            document.getElementById('name').disabled  = false;
            document.getElementById('name').value  = "";
            document.getElementById('type').value  = "";
            document.getElementById('local_ip').value  = "";
            document.getElementById('local_port').value  = "";
            document.getElementById('remote_port').value  = "";
        }
        function del(name){
            bootbox.confirm("确认删除 " + name, function (result) {
                if(result){
                    var reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
                    var r = window.location.search.substr(1).match(reg);
                    if (r == null){
                        r = ['127.0.0.1','127.0.0.1','127.0.0.1'];
                    }
                    const Http = new XMLHttpRequest();
                    var rul = catrul("frpc/api?");
                    Http.open("GET",rul + '&type=del' + '&name=' + name);
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
                                        var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
                                        document.getElementById('logs').src = rul;
                                    }
                            }
                        }
                    }
                }
            })
        }
        function addpost(){
            var reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
            var r = window.location.search.substr(1).match(reg);
            if (r == null){
                r = ['127.0.0.1','127.0.0.1','127.0.0.1'];
            }
            edit = document.getElementById('h3text').innerHTML;
            name = document.getElementById('name').value;
            id = document.getElementById('id').value;
            type = document.getElementById('type').value;
            local_ip = document.getElementById('local_ip').value;
            local_port = document.getElementById('local_port').value;
            remote_port = document.getElementById('remote_port').value;
            const Http = new XMLHttpRequest();
            var rul = catrul("frpc/api?");
            Http.open("GET",rul + '&id=' + id + '&type=' + edit + '&name=' + name + '&types=' + type + '&local_ip=' + local_ip + '&local_port=' + local_port + '&remote_port=' + remote_port);
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
                                var rul = catrul("main/tty?") + "&sw=/frpc/logs&bash=logs";
                                document.getElementById('logs').src = rul;
                            }
                    }
                }
            }
        }
        function edit(name){
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
                                if (data.data[i].name == document.getElementById('name').value)
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
        function up_post(data){
            if (data == "start"){
                document.getElementById('start').disabled  = true;
                const Http = new XMLHttpRequest();
                var rul = catrul("frpc/api?");
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
                var rul = catrul("frpc/api?");
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
                var rul = catrul("frpc/api?");
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
        function up_biao() {
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
                            if (data.run == "run" ){
                                str = '<p>\
                                        <button class="btn " onclick="window.open(\'http://\' + window.location.hostname + \':8080\');return false;;return false;">在新窗口打开</button> .\
                                    </p>';
                                //document.getElementById('tab1n').innerHTML = str;
                                
                                document.getElementById('start').innerHTML  = "停止程序";
                                document.getElementById('start').onclick  = function(){up_post('stop');};
                            }else{
                                str = '<p>\
                                        <button class="btn " onclick="up_biao();return false;">未在运行,点击刷新</button> \
                                    </p>';
                                //document.getElementById('tab1n').innerHTML = str;
                                
                                document.getElementById('start').innerHTML  = "启动程序";
                                document.getElementById('start').onclick  = function(){up_post('start');};
                            }
                            if (data.boot == "yes"){
                                document.getElementById('boot').innerHTML  = "自启:开启";
                                document.getElementById('boot').onclick  = function(){up_post('bootoff');};
                            }else{
                                document.getElementById('boot').innerHTML  = "自启:关闭";
                                document.getElementById('boot').onclick  = function(){up_post('booton');};
                            }
                            
                            document.getElementById('server').value  = data.common.server_addr;
                            document.getElementById('port').value  = data.common.server_port;
                            document.getElementById('token').value  = data.common.token;
                            document.getElementById('admin_addr').value  = data.common.admin_addr;
                            document.getElementById('admin_port').value  = data.common.admin_port;
                            document.getElementById('admin_user').value  = data.common.admin_user;
                            document.getElementById('admin_pwd').value  = data.common.admin_pwd;

                            var reg = "";
                            var link = "";
                            for (i = 0; i < data.datafo; i++) {
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
                                reg = reg + '<a href="' + '' + 'api?link=' + r[2] + '" id="' + servername + "mini" + '">' + data.data[i].name + '</a>';
                                reg = reg + '</td>';
                                reg = reg + '<td id="' + servername + "info" + '">';
                                reg = reg + data.data[i].local_ip + ":" + data.data[i].local_port;
                                reg = reg + '</td>';
                                reg = reg + '<td id="' + servername + "info" + '">';
                                reg = reg + data.data[i].remote_port;
                                reg = reg + '</td>';
                                reg = reg + '<td id="' + servername + "info" + '">';
                                reg = reg + data.data[i].run;
                                reg = reg + '</td>';
                                reg = reg + '<td>\
                                                <button class="btn btn-xs btn-success" data-toggle="modal" data-target="#my-modal" onclick="edit(\'' + data.data[i].name + '\');">\
                                                    <!--i class="ace-icon fa fa-download bigger-120"></i-->修改\
                                                </button>\
                                                <button class="btn btn-xs btn-danger" data-toggle="modal" onclick="del(\'' + data.data[i].name + '\');">\
                                                    <!--i class="ace-icon fa fa-download bigger-120"></i-->删除\
                                                </button>\
                                        </td >';
                                reg = reg + '</tr>';
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
