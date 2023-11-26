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
                    <?php include 'main/wutz.html'; ?>

                    <li class="light-blue dropdown-modal">
                        <a data-toggle="dropdown" href="#" class="dropdown-toggle">
                            <img class="nav-user-photo" src="assets/images/avatars/user.jpg" alt="Jason's Photo" />
                            <span class="user-info">
                                <small>欢迎,</small>
                                <?php echo $user; ?>
                            </span>

                            <i class="ace-icon fa fa-caret-down"></i>
                        </a>

                        <?php include 'main/usercaidan.html'; ?>
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
                        <li class="active"><div id="biaotou">集群管理</li>
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
                    <?php include 'main/ace-settings-container.html'; ?>
                    <div id="row" class="row tab-content" style="border:0px solid #C5D0DC;padding: 0px 0px;">
                        <div id='main' class="col-xs-12 tab-pane fade active in">
                            <!-- PAGE CONTENT BEGINS -->
                            <div class="table-header ">
                                节点列表
								<a id="aadd" data-toggle="tab" href='#add' class="fade">add</a>
								<a id="amain" data-toggle="tab" href='#main' class="fade">main</a>
								<a id="sxx" data-toggle="tab" href='#main' class="fade">1</a>
                                <button id="bootbox-options" data-toggle="tab" role="button" class="pull-right btn btn-sm btn-success " data-dismiss="modal" formaction="#modal-table" onclick="document.getElementById('aadd').click();">
                                    
                                    添加
                                </button>
                            </div>
                            <!-- PAGE CONTENT BEGINS -->
                            <div class="row">
                                <div class="col-xs-12">
                                    <table id="simple-table" class="table  table-bordered table-hover">
                                        <thead id="biaotou1">
                                            <tr>
                                                <th class="detail-col">
                                                    <label class="pos-rel">
                                                        <input type="checkbox" class="ace" />
                                                        <span class="lbl"></span>
                                                    </label>
                                                </th>
                                                <th class="hidden-480">节点名称</th>
                                                <th class="detail-col">受控端</th>
                                                <th class="detail-col">安全</th>
                                                <th class="hidden-480" style="width: 10%;">CPU</th>
                                                <th class="hidden-480">内存</th>
                                                <th class="hidden-480">存储</th>
                                                <th class="hidden-480">网络</th>
                                                <th class="hidden-480">操作</th>
                                            </tr>
                                        </thead>

                                        <tbody id="biaoinfo">
                                        </tbody>

                                    </table>
                                </div><!-- /.span -->
                            </div><!-- /.row -->
                            <!-- PAGE CONTENT ENDS -->
                        </div><!-- /.col -->
                        <div id='add' class="col-xs-12 tab-pane fade ">
                        <form class="form-horizontal" role="form">
									<div class="form-group">
										<label class="col-sm-3 control-label no-padding-right" for="form-field-1"> 节点名称 </label>

										<div class="col-sm-9">
											<input type="text" id="form-field-1" placeholder="默认为地址" class="col-xs-10 col-sm-5" name="devname">
										</div>
									</div>
									<div class="form-group">
										<label class="col-sm-3 control-label no-padding-right" for="form-field-1"> 网络地址 </label>

										<div class="col-sm-9">
											<input type="text" id="form-field-1" placeholder="输入地址,自动识别http/https" class="col-xs-10 col-sm-5" name="devrul">
										</div>
									</div><div class="form-group">
										<label class="col-sm-3 control-label no-padding-right" for="form-field-1"> 端口 </label>

										<div class="col-sm-9">
											<input type="text" id="form-field-1" placeholder="8888" class="col-xs-10 col-sm-5" name="devport">
										</div>
									</div>
									<div class="form-group">
										<label class="col-sm-3 control-label no-padding-right" for="form-field-1"> 用户名 </label>

										<div class="col-sm-9">
											<input type="text" id="form-field-1" placeholder="user" class="col-xs-10 col-sm-5" name="devuser">
										</div>
									</div>
									<div class="form-group">
										<label class="col-sm-3 control-label no-padding-right" for="form-field-1"> 密码 </label>

										<div class="col-sm-9">
											<input type="text" id="form-field-1" placeholder="password" class="col-xs-10 col-sm-5" name="devpassword">
										</div>
									</div>

									<div class="clearfix form-actions">
										<div class="col-md-offset-3 col-md-9 pull-right">
											<button class="btn btn-info" type="button" onclick="addpost();return false;">
												<i class="ace-icon fa fa-check bigger-110"></i>
												确定
											</button>

											&nbsp; &nbsp; &nbsp;
											<button class="btn" type="reset" onclick="document.getElementById('amain').click();">
												<i class="ace-icon fa fa-undo bigger-110"></i>
												取消
											</button>
										</div>
									</div>

									<div class="hr hr-24"></div>

									
								</form>
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

    <!-- page specific plugin scripts -->
    <!-- ace scripts -->
    <script src="assets/js/ace-elements.min.js"></script>
    <script src="assets/js/ace.min.js"></script>
    <script src="assets/js/bootbox.js"></script>
    <script src="main/index.js"></script>
    <script src="index.js"></script>
    <script type="text/javascript">
        jQuery(function ($) {
            /////////////////////////////////
            //表复选框
            $('th input[type=checkbox], td input[type=checkbox]').prop('checked', false);

            //选中/取消选择"根据表头选择所有行"复选框
            $('#dynamic-table > thead > tr > th input[type=checkbox], #dynamic-table_wrapper input[type=checkbox]').eq(0).on('click', function () {
                var th_checked = this.checked;//checkbox inside "TH" table header

                $('#dynamic-table').find('tbody > tr').each(function () {
                    var row = this;
                    if (th_checked) myTable.row(row).select();
                    else myTable.row(row).deselect();
                });
            });

            //选中/取消选中复选框时选择/取消选择行
            $('#dynamic-table').on('click', 'td input[type=checkbox]', function () {
                var row = $(this).closest('tr').get(0);
                if (this.checked) myTable.row(row).deselect();
                else myTable.row(row).select();
            });

        })
    </script>
    <script type="text/javascript">
        window.onload = function () {
            //jcminit();
            
        }

        function addpost() {
            var devname = $('input[name=devname]').val();
            var devrul = $('input[name=devrul]').val();
            var devuser = $('input[name=devuser]').val();
            var devpassword = $('input[name=devpassword').val();
            var devport = $('input[name=devport').val();
            if (!devrul) {
                bootbox.confirm("地址不能为空", function (result) {

                })
                //layer.msg("用户名不能为空");
                return false;
            }if (!devuser) {
                bootbox.confirm("用户名不能为空", function (result) {

                })
                //layer.msg("用户名不能为空");
                return false;
            }if (!devpassword) {
                bootbox.confirm("密码不能为空", function (result) {

                })
                //layer.msg("用户名不能为空");
                return false;
            }if (!devname) {
                devname = devrul;
                //layer.msg("用户名不能为空");
            }if (!devport) {
                devport = 8888;
                //layer.msg("用户名不能为空");
            }
            //var auto = false;
            //if (checkbox.checked)
            var data =
                { devname: devname, devrul: devrul, devuser: devuser ,devpassword: devpassword ,devport: devport };
            $.ajax({
                url: "main/add",
                type: 'post',
                async: true,
                data: data,
                dataType: "json",
                success: function (data) {
                    if (data.data == "添加成功"){
                        location.reload();
                    }
                    bootbox.confirm(data.data, function (result) {

                    })
                    re_captcha();
                },
                error: function () {
                    bootbox.confirm("链接失败", function (result) {

                    })
                    re_captcha();
                }

            })
        }
    </script>

    <!-- inline scripts related to this page -->
</body>
</html>
