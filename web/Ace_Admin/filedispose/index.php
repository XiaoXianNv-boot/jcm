<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta charset="utf-8" />
    <title id="title">集群管理</title>

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
            <div style="display:none;">
                <div id="dir"><?php echo $_POST['dir']; ?></div>
                <div id="file"><?php echo $_POST['file']; ?></div>
            </div>

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
                        <li class="active"><div id="biaotou"><?php echo $_POST['dir']; ?></div></li>
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
                        <div class="tabbable" >
                            <ul class="nav nav-tabs" id="myTab">
                                <li style="float: right">
                                    <a data-toggle="tab" href="#tabdata" onclick="click:addtab();return false;">
                                        &nbsp;&nbsp;&nbsp;&nbsp;添加 &nbsp;&nbsp;&nbsp;&nbsp;
                                    </a>
                                </li>
                                <li id="tab1nn" class="active">				            
                                    <a data-toggle="tab" href="#tab1n" id="tab1" aria-expanded="true">					            
                                        <i class="green ace-icon fa fa-home bigger-120"></i>					            
                                        Home				            
                                    </a>			            
                                </li>
                                <li id="tab2nn" class="">				            
                                    <a data-toggle="tab" href="#tab2n" id="tab2" aria-expanded="true">					            
                                        处理进程				            
                                    </a>			            
                                </li>
                                <li class="">				            
                                    <a data-toggle="tab" href="#tab3n" id="tab3" aria-expanded="true">					            
                                        输入目录				            
                                    </a>			            
                                </li>
                                <li class="">				            
                                    <a data-toggle="tab" href="#tab4n" id="tab4" aria-expanded="true">					            
                                        输出目录				            
                                    </a>			            
                                </li>
                                <li class="">				            
                                    <a data-toggle="tab" href="#tab5n" id="tab5" aria-expanded="true">					            
                                        默认目录				            
                                    </a>			            
                                </li>
                            </ul>
                            <div class="tab-content" style="height: 100%;" id="tabn">
                                <div id="tabdata" class="tab-pane fade">
                                    <div id="tabs"></div>
                                </div>
                                <div id="tab1n" class="tab-pane fade active in">				            
                                    <p>
                                        <button class="btn " onclick="run();return false;">开始</button> 
                                    </p>			            
                                </div>
                                <div id="tab2n" class="tab-pane fade">
                                    <div class="">
                                        <!-- PAGE CONTENT BEGINS -->
                                        <div class="table-header">
                                            状态：
                                            <text id="linktext">断开</text>
                                              数量：
                                            <text id="runtext">0</text>
                                            <text id="runtextx"></text>
                                            <!--a href="#my-modal" role="button" class="pull-right green" data-toggle="modal"-->
                                                <button id="bootbox-options" class="pull-right btn btn-sm btn-danger" data-toggle="modal" data-target="#my-modal" onclick="mv();">
                                                    <!--i class="ace-icon fa fa-times"></i-->
                                                    开始移动文件
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
                                                            <th class="hidden-480">目录</th>
                                                            <th class="hidden-480">操作</th>
                                                        </tr>
                                                    </thead>

                                                    <tbody id="biaoinfo">
                                                        

                                                    </tbody>
                                                    <div id="data" style="display:none;"></div>
                                                </table>
                                            </div><!-- /.span -->
                                        </div><!-- /.row -->
                                        
                                        <!-- PAGE CONTENT ENDS -->
                                    </div><!-- /.col -->
                                </div>
                                <div id="tab3n" class="tab-pane fade">
                                    <div class="">
                                        <!-- PAGE CONTENT BEGINS -->
                                        <div class="table-header">
                                        输入目录
                                            <!--a href="#my-modal" role="button" class="pull-right green" data-toggle="modal"-->
                                                <button id="bootbox-options" class="pull-right btn btn-sm btn-danger" data-toggle="modal" data-target="#my-modal" onclick="addindir();">
                                                    <!--i class="ace-icon fa fa-times"></i-->
                                                    添加
                                                </button>
                                                <input class="pull-right input-sm" type="text" id="addindir" name="addindir" placeholder="/root/in or C:/in">
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
                                                            <th class="">目录</th>
                                                            <th class="detail-col">状态</th>
                                                            <th class="detail-col">操作</th>
                                                        </tr>
                                                    </thead>

                                                    <tbody id="biaoinfoinml">
                                                        

                                                    </tbody>

                                                </table>
                                            </div><!-- /.span -->
                                        </div><!-- /.row -->
                                        
                                        <!-- PAGE CONTENT ENDS -->
                                    </div><!-- /.col -->
                                </div>
                                <div id="tab4n" class="tab-pane fade">
                                    <div class="">
                                        <!-- PAGE CONTENT BEGINS -->
                                        <div class="table-header">
                                        输出目录
                                            <!--a href="#my-modal" role="button" class="pull-right green" data-toggle="modal"-->
                                            
                                                <button id="bootbox-options" class="pull-right btn btn-sm btn-danger" data-toggle="modal" data-target="#my-modal" onclick="addoutdir();">
                                                    <!--i class="ace-icon fa fa-times"></i-->
                                                    添加
                                                </button>
                                                <input class="pull-right input-sm" name="addoutdir" type="text" id="form-field-4" placeholder="/root/out or C:/out">
                                                <input class="pull-right input-sm" name="name" type="text" id="form-field-4" placeholder="name">
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
                                                            <th class="">名称</th>
                                                            <th class="">目录</th>
                                                            <th class="">总空间/剩余空间</th>
                                                            <th class="detail-col">状态</th>
                                                            <th class="detail-col">操作</th>
                                                        </tr>
                                                    </thead>

                                                    <tbody id="biaoinfooutml">
                                                        

                                                    </tbody>

                                                </table>
                                            </div><!-- /.span -->
                                        </div><!-- /.row -->
                                        
                                        <!-- PAGE CONTENT ENDS -->
                                    </div><!-- /.col -->
                                </div>
                                <div id="tab5n" class="tab-pane fade">
                                    <div class="">
                                        <!-- PAGE CONTENT BEGINS -->
                                        <div class="table-header">
                                        默认目录
                                            <!--a href="#my-modal" role="button" class="pull-right green" data-toggle="modal"-->
                                            
                                                <button id="bootbox-options" class="pull-right btn btn-sm btn-danger" data-toggle="modal" data-target="#my-modal" onclick="addddir();">
                                                    <!--i class="ace-icon fa fa-times"></i-->
                                                    添加
                                                </button>
                                                <input class="pull-right input-sm" name="ddir" type="text" id="form-field-4" placeholder="dir">
                                                <input class="pull-right input-sm" name="dname" type="text" id="form-field-4" placeholder="name">
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
                                                            <th class="">后缀名</th>
                                                            <th class="">目录</th>
                                                            <th class="detail-col">操作</th>
                                                        </tr>
                                                    </thead>

                                                    <tbody id="biaoinfod">
                                                        

                                                    </tbody>

                                                </table>
                                            </div><!-- /.span -->
                                        </div><!-- /.row -->
                                        
                                        <!-- PAGE CONTENT ENDS -->
                                    </div><!-- /.col -->
                                </div>
                            </div>
                        </div>
                        <script type="text/javascript">
                            //function index(){
                                document.getElementById("biaotou").innerHTML = "文件处理";
                            //}
                        </script>
                    </div><!-- /.row -->
                </div><!-- /.page-content -->
            </div>
        </div><!-- /.main-content -->

        <?php include '../main/footer.html'; ?>
        <div id="link" style="display:none;"><?php echo $_POST['link']; ?></div>
        <div id="du" style="display:none;"><?php echo $_POST['du']; ?></div>

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
    <script src="index.js"></script>
    <script src="filedispose/index.js"></script>
    <script type="text/javascript">
        jQuery(function ($) {

        })
    </script>
    <script type="text/javascript">
        window.onload = function () {
            const Http = new XMLHttpRequest();
            var rul = catrul("filedispose/api?");
            /*Http.open("GET",rul + '&type=index');
            Http.send();
            Http.onreadystatechange = (e) => {
                if(Http.readyState == 4){
                    if (Http.status == 200) {
                        document.getElementById('row').innerHTML = Http.responseText;
                        index();
                    }else if (Http.status == 401) {
                        location.reload();
                    }else{
                        document.getElementById('row').innerHTML = Http.responseText;
                    }
                }
            }*/

        }


    </script>

    <!-- inline scripts related to this page -->
    
</body>
</html>









