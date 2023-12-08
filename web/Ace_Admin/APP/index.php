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

                    <div class="row">
                        <div class="col-xs-12">
                            <!-- PAGE CONTENT BEGINS -->
                            <div class="table-header">
                                应用商店
                                <!--a href="#my-modal" role="button" class="pull-right green" data-toggle="modal"-->
                                    <button id="bootbox-options" class="pull-right btn btn-sm btn-danger" data-toggle="modal" data-target="#my-modal" onclick="values('updata');">
                                        <!--i class="ace-icon fa fa-times"></i-->
                                        刷新
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
                                                <th class="hidden-480">软件名称</th>
                                                <th class="detail-col">介绍</th>
                                                <th class="hidden-480">操作</th>
                                            </tr>
                                        </thead>

                                        <tbody id="biaoinfo">
                                            

                                        </tbody>

                                    </table>
                                </div><!-- /.span -->
                            </div><!-- /.row -->
                            <div id="my-modal" class="modal fade" tabindex="-1" data-backdrop=false >
                                <div class="modal-dialog" style="width: 100%; height: 908px;">
                                    <div class="modal-content" >
                                        <div class="modal-header">
                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true" onclick="up_biao()">&times;</button>
                                            <h3 class="smaller lighter blue no-margin"><div id="h3text">update</div></h3>
                                        </div>

                                        <div class="modal-body">
                                            <iframe id="tty" src="/?" width="100%" height="500"></iframe>
                                        </div>

                                        <div class="modal-footer">
                                            <button class="btn btn-sm btn-danger pull-right" data-dismiss="modal" onclick="up_biao()">
                                                <i class="ace-icon fa fa-times"></i>
                                                Close
                                            </button>
                                        </div>
                                    </div><!-- /.modal-content -->
                                </div><!-- /.modal-dialog -->
                            </div>
                            <!-- PAGE CONTENT ENDS -->
                        </div><!-- /.col -->
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

            $('#my-modal').on('shown.bs.modal',
                function() {
                    var reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
                    var r = window.location.search.substr(1).match(reg);
                    if (r == null){
                        r = ['127.0.0.1','127.0.0.1','127.0.0.1'];
                    }
                    document.getElementById('tty').src = 'main/tty?link=' + r[2] + '&sw=/APP/pkg&bash=' + document.getElementById('h3text').innerHTML;
                    
                })
            //$('[data-rel=tooltip]').tooltip();
        })
        function values(ID){
            document.getElementById('h3text').innerHTML = ID;
        }
    </script>
    <script type="text/javascript">
        window.onload = function () {
            //userinit();
            if (document.body.clientWidth <= 600) {
                str = '<tr>'
                str += '  <th class="detail-col" >'
                str += '    <label class="pos-rel">'
                str += '      <input type="checkbox" class="ace" />'
                str += '      <span class="lbl"></span>'
                str += '    </label>'
                str += '  </th >'
                str += '  <th class="">软件名称</th>'
                str += '  <th class="">介绍</th>'
                //str += '  <th class="detail-col">安全</th>'
                //str += '  <th class="hidden-480">CPU</th>'
                //str += '  <th class="hidden-480">内存</th>'
                //str += '  <th class="hidden-480">存储</th>'
                //str += '  <th class="hidden-480">网络</th>'
                str += '  <th class="detail-col">操作</th>'
                str += '</tr >'
                document.getElementById('biaotou').innerHTML = str;
            }
            up_biao();
        }
        function up_biao() {
            const Http = new XMLHttpRequest();
            var reg = new RegExp("(^|&)" + "link" + "=([^&]*)(&|$)", "i");
            var r = window.location.search.substr(1).match(reg);
            if (r == null){
                r = ['127.0.0.1','127.0.0.1','127.0.0.1'];
            }
            document.getElementById('tty').src = 'about:blank';
            Http.open("GET", 'APP/info?link=' + r[2]);
            Http.send();
            Http.onreadystatechange = (e) => {
                if(Http.readyState == 4 && Http.status == 200){
                    if (Http.status == 200) {
                        cathttp = Http.responseText;
                        if (cathttp.substr(0, 1) == "<") {
                            location.reload();
                        } else {
                            var data = JSON.parse(cathttp);
                            str = '<tr>'
                            str += '  <th class="detail-col" >'
                            str += '    <label class="pos-rel">'
                            str += '      <input type="checkbox" class="ace" />'
                            str += '      <span class="lbl"></span>'
                            str += '    </label>'
                            str += '  </th >'
                            str += '  <th class="">软件名称</th>'
                            str += '  <th class="">介绍</th>'
                            str += '  <th class="detail-col">操作</th>'
                            str += '</tr >' 
                            document.getElementById('biaotou').innerHTML = str;
                            var reg = "";
                            var link = "";
                            for (i = 0; i < data.for; i++) {
                                servername = data.server[i].Package
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
                                reg = reg + '<a href="' + '' + 'api?link=' + r[2] + '" id="' + servername + "mini" + '">' + data.server[i].name + '</a>';
                                reg = reg + '</td>';
                                reg = reg + '<td id="' + servername + "info" + '">';
                                reg = reg + data.server[i].Description;
                                reg = reg + '</td>';
                                reg = reg + '<td>\
                                                <button class="btn btn-xs btn-success" data-toggle="modal" data-target="#my-modal" onclick="values(\'install_' + data.server[i].Package + '\');">\
                                                    <!--i class="ace-icon fa fa-download bigger-120"></i-->安装\
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
