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

								<li style="float: right">
									<a data-toggle="tab" href="#tabdata" onclick="click:addtab();return false;">
										&nbsp;&nbsp;&nbsp;&nbsp;添加 &nbsp;&nbsp;&nbsp;&nbsp;
									</a>
								</li>
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
                                    <p>
                                        <button class="btn ">正在加载</button>
                                    </p>			            
                                </div>
								<div id="tab2n" class="tab-pane fade in">				            
                                    <p>
                                    <button class="btn ">正在加载</button>
                                    </p>			            
                                </div>
								<div id="tab3n" class="tab-pane fade in">				            
                                    		            
                                </div>
                            </div>
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
            var rul = catrul("frpc/logs?");
            document.getElementById('tab3n').innerHTML = '<iframe src="' + rul + '" width="100%" height="100%"></iframe>	';
            
        }
        function up_post(data){
            if (data == "start"){
                const Http = new XMLHttpRequest();
                var rul = catrul("frpc/api?");
                Http.open("GET",rul + '&type=start');
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
                                    var rul = catrul("frpc/logs?");
                                    bootbox.confirm(data.data + '<iframe src="' + rul + '" width="100%" height="100%"></iframe>	', function (result) {

                                    })
                                }else{
                                    
                                    bootbox.confirm(data.data, function (result) {

                                    })
                                }
                                up_biao();
                                var rul = catrul("frpc/logs?");
                                document.getElementById('tab3n').innerHTML = '<iframe src="' + rul + '" width="100%" height="100%"></iframe>	';
                            }
                        }
                    }
                }
            }
        }
        function up_biao() {
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
                                document.getElementById('tab1n').innerHTML = str;
                                str = '<p>\
                                        <button class="btn " onclick="up_post("stop");return false;">停止程序</button> \
                                    </p>';
                                document.getElementById('tab2n').innerHTML = str;
                            }else{
                                str = '<p>\
                                        <button class="btn " onclick="up_biao();return false;">未在运行,点击刷新</button> \
                                    </p>';
                                document.getElementById('tab1n').innerHTML = str;
                                str = '<p>\
                                        <button class="btn " onclick="up_post(\'start\');return false;">启动程序</button> \
                                    </p>';
                                document.getElementById('tab2n').innerHTML = str;
                                
                            }
                            
                            
                        }
                    }
                }
            }
        }
    </script>

    <!-- inline scripts related to this page -->
    
</body>
</html>
