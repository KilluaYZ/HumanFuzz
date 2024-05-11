def getRegisterEmail(userName: str, token: str):
    html_str1 = """
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div id="contentDiv" onmouseover="getTop().stopPropagation(event);"
        onclick="getTop().preSwapLink(event, 'html', 'ZC0025_DQbNu8yM1LYu1GQA0GRhvd6');"
        style="position:relative;font-size:14px;height:auto;padding:15px 15px 10px 15px;z-index:1;zoom:1;line-height:1.7;"
        class="body">
        <div id="qm_con_body">
            <div id="mailContentContainer" class="qmbox qm_con_body_content qqmail_webmail_only" style="opacity: 1;">
                <style type="text/css" media="screen">
                    @font-face {
                        font-family: 'Motiva Sans';
                        font-style: normal;
                        font-weight: 300;
                        src: local('Motiva Sans'), url('https://store.akamai.steamstatic.com/public/shared/fonts/email/MotivaSans-Light.woff') format('woff');
                    }

                    @font-face {
                        font-family: 'Motiva Sans';
                        font-style: normal;
                        font-weight: normal;
                        src: local('Motiva Sans'), url('https://store.akamai.steamstatic.com//public/shared/fonts/email/MotivaSans-Regular.woff') format('woff');
                    }

                    @font-face {
                        font-family: 'Motiva Sans';
                        font-style: normal;
                        font-weight: bold;
                        src: local('Motiva Sans'), url('https://store.akamai.steamstatic.com//public/shared/fonts/email/MotivaSans-Bold.woff') format('woff');
                    }

                    .qmbox [style*='Motiva Sans'] {
                        font-family: 'Motiva Sans', Arial, sans-serif !important;
                    }
                </style>
                <style type="text/css" media="screen">
                    .qmbox body {
                        padding: 0 !important;
                        margin: 0 auto !important;
                        display: block !important;
                        min-width: 100% !important;
                        width: 100% !important;
                        background: #ffffff;
                        -webkit-text-size-adjust: none;
                    }

                    .qmbox a {
                        color: #7abefa;
                        text-decoration: underline;
                    }

                    .qmbox body a {
                        color: #ffffff;
                        text-decoration: underline;
                    }

                    .qmbox img {
                        margin: 0 !important;
                        -ms-interpolation-mode: bicubic;
                        /* Allow smoother rendering of resized image in Internet Explorer */
                    }

                    /* for recepits */
                    .qmbox table {
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                    }

                    .qmbox img,
                    .qmbox a img {
                        border: 0;
                        outline: none;
                        text-decoration: none;
                    }

                    .qmbox #outlook a {
                        padding: 0;
                    }

                    .qmbox .ReadMsgBody {
                        width: 100%;
                    }

                    .qmbox .ExternalClass {
                        width: 100%;
                    }

                    .qmbox div,
                    .qmbox p,
                    .qmbox a,
                    .qmbox li,
                    .qmbox td,
                    .qmbox blockquote {
                        mso-line-height-rule: exactly;
                    }

                    .qmbox a[href^=tel],
                    .qmbox a[href^=sms] {
                        color: inherit;
                        text-decoration: none;
                    }

                    .qmbox .ExternalClass,
                    .qmbox .ExternalClass p,
                    .qmbox .ExternalClass td,
                    .qmbox .ExternalClass div,
                    .qmbox .ExternalClass span,
                    .qmbox .ExternalClass font {
                        line-height: 100%;
                    }

                    /* END for recepits */

                    .qmbox a[x-apple-data-detectors] {
                        color: inherit !important;
                        text-decoration: inherit !important;
                        font-size: inherit !important;
                        font-family: inherit !important;
                        font-weight: inherit !important;
                        line-height: inherit !important;
                    }

                    .qmbox .btn-18 a {
                        display: block;
                        padding: 13px 35px;
                        text-decoration: none;
                    }

                    .qmbox .l-white a {
                        color: #ffffff;
                    }

                    .qmbox .l-black a {
                        color: #000001;
                    }

                    .qmbox .l-grey1 a {
                        color: #dbdee2;
                    }

                    .qmbox .l-grey2 a {
                        color: #a1a2a4;
                    }

                    .qmbox .l-grey3 a {
                        color: #dadcdd;
                    }

                    .qmbox .l-grey4 a {
                        color: #f1f1f1;
                    }

                    .qmbox .l-grey5 a {
                        color: #dddedf;
                    }

                    .qmbox .l-grey6 a {
                        color: #bfbfbf;
                    }

                    .qmbox .l-grey7 a {
                        color: #dcdddd;
                    }

                    .qmbox .l-grey8 a {
                        color: #8e96a4;
                    }

                    .qmbox .l-green a {
                        color: #a4d007;
                    }

                    .qmbox .l-blue a {
                        color: #6a7c96;
                    }

                    .qmbox .l-blue1 a {
                        color: #7abefa;
                    }

                    .qmbox .l-blue2 a {
                        color: #9eb8cc;
                    }


                    /* Mobile styles */
                    @media only screen and (max-device-width: 480px),
                    only screen and (max-width: 480px) {
                        .qmbox .mpy-35 {
                            padding-top: 35px !important;
                            padding-bottom: 35px !important;
                        }

                        .qmbox .mpx-15 {
                            padding-left: 15px !important;
                            padding-right: 15px !important;
                        }

                        .qmbox .mpx-20 {
                            padding-left: 20px !important;
                            padding-right: 20px !important;
                        }

                        .qmbox .mpb-30 {
                            padding-bottom: 30px !important;
                        }

                        .qmbox .mpb-10 {
                            padding-bottom: 10px !important;
                        }

                        .qmbox .mpb-15 {
                            padding-bottom: 15px !important;
                        }

                        .qmbox .mpb-20 {
                            padding-bottom: 20px !important;
                        }

                        .qmbox .mpb-35 {
                            padding-bottom: 35px !important;
                        }

                        .qmbox .mpb-40 {
                            padding-bottom: 40px !important;
                        }

                        .qmbox .mpb-50 {
                            padding-bottom: 50px !important;
                        }

                        .qmbox .mpb-60 {
                            padding-bottom: 60px !important;
                        }

                        .qmbox .mpt-30 {
                            padding-top: 30px !important;
                        }

                        .qmbox .mpt-40 {
                            padding-top: 40px !important;
                        }

                        .qmbox .mpy-40 {
                            padding-top: 40px !important;
                            padding-bottom: 40px !important;
                        }

                        .qmbox .mpt-0 {
                            padding-top: 0px !important;
                        }

                        .qmbox .mpr-0 {
                            padding-right: 0px !important;
                        }

                        .qmbox .mfz-14 {
                            font-size: 14px !important;
                        }

                        .qmbox .mfz-28 {
                            font-size: 28px !important;
                        }

                        .qmbox .mfz-16 {
                            font-size: 16px !important;
                        }

                        .qmbox .mfz-24 {
                            font-size: 24px !important;
                        }

                        .qmbox .mlh-18 {
                            line-height: 18px !important;
                        }

                        .qmbox u+body .gwfw {
                            width: 100% !important;
                            width: 100vw !important;
                        }

                        .qmbox .td,
                        .qmbox .m-shell {
                            width: 100% !important;
                            min-width: 100% !important;
                        }

                        .qmbox .mt-left {
                            text-align: left !important;
                        }

                        .qmbox .mt-center {
                            text-align: center !important;
                        }

                        .qmbox .mt-right {
                            text-align: right !important;
                        }

                        .qmbox .m-left {
                            text-align: left !important;
                        }

                        .qmbox .me-left {
                            margin-right: auto !important;
                        }

                        .qmbox .me-center {
                            margin: 0 auto !important;
                        }

                        .qmbox .me-right {
                            margin-left: auto !important;
                        }

                        .qmbox .mh-auto {
                            height: auto !important;
                        }

                        .qmbox .mw-auto {
                            width: auto !important;
                        }

                        .qmbox .fluid-img img {
                            width: 100% !important;
                            max-width: 100% !important;
                            height: auto !important;
                        }

                        .qmbox .column,
                        .qmbox .column-top,
                        .qmbox .column-dir,
                        .qmbox .column-dir-top {
                            float: left !important;
                            width: 100% !important;
                            display: block !important;
                        }

                        .qmbox .kmMobileStretch {
                            float: left !important;
                            width: 100% !important;
                            display: block !important;
                            padding-left: 0 !important;
                            padding-right: 0 !important;
                        }

                        .qmbox .m-hide {
                            display: none !important;
                            width: 0 !important;
                            height: 0 !important;
                            font-size: 0 !important;
                            line-height: 0 !important;
                            min-height: 0 !important;
                        }

                        .qmbox .m-block {
                            display: block !important;
                        }

                        .qmbox .mw-15 {
                            width: 15px !important;
                        }

                        .qmbox .mw-2p {
                            width: 2% !important;
                        }

                        .qmbox .mw-32p {
                            width: 32% !important;
                        }

                        .qmbox .mw-49p {
                            width: 49% !important;
                        }

                        .qmbox .mw-50p {
                            width: 50% !important;
                        }

                        .qmbox .mw-100p {
                            width: 100% !important;
                        }

                        .qmbox .mbgs-200p {
                            background-size: 200% auto !important;
                        }
                    }
                </style>
                <center>
                    <table width="100%" border="0" cellspacing="0" cellpadding="0"
                        style="margin: 0; padding: 0; width: 100%; height: 100%;" bgcolor="#ffffff" class="gwfw">
                        <tbody>
                            <tr>
                                <td style="margin: 0; padding: 0; width: 100%; height: 100%;" align="center"
                                    valign="top">
                                    <table width="775" border="0" cellspacing="0" cellpadding="0" class="m-shell">
                                        <tbody>
                                            <tr>
                                                <td class="td"
                                                    style="width:775px; min-width:775px; font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">

                                                        <tbody>
                                                            <tr>
                                                                <td class="p-80 mpy-35 mpx-15" bgcolor="#212429"
                                                                    style="padding: 80px;">
                                                                    <table width="100%" border="0" cellspacing="0"
                                                                        cellpadding="0">


                                                                        <tbody>
                                                                            <tr>
                                                                                <td class="img pb-45"
                                                                                    style="font-size:0pt; line-height:0pt; text-align:left; padding-bottom: 45px;">
                                                                                    <a href="https://info.ruc.edu.cn/"
                                                                                        target="_blank" rel="noopener">
                                                                                        <!-- <img src="http://info.ruc.edu.cn/images/logo.png"
                                                                                            width="265" height="88"
                                                                                            border="0"> -->
                                                                                    </a>

                                                                                </td>
                                                                            </tr>
    """

    html_str2 = f"""
                                                                            <tr>
                                                                                <td>
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="title-36 pb-30 c-grey6 fw-b"
                                                                                                    style="font-size:36px; line-height:42px; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left; padding-bottom: 30px; color:#bfbfbf; font-weight:bold;">
                                                                                                    {userName}，您好！</td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="text-18 c-grey4 pb-30"
                                                                                                    style="font-size:18px; line-height:25px; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left; color:#dbdbdb; padding-bottom: 30px;">
                                                                                                    您注册帐户 {userName} 所需的令牌验证码为：</td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="pb-70 mpb-50"
                                                                                                    style="padding-bottom: 70px;">
                                                                                                    <table width="100%"
                                                                                                        border="0"
                                                                                                        cellspacing="0"
                                                                                                        cellpadding="0"
                                                                                                        bgcolor="#17191c">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td class="py-30 px-56"
                                                                                                                    style="padding-top: 30px; padding-bottom: 30px; padding-left: 56px; padding-right: 56px;">
                                                                                                                    <table
                                                                                                                        width="100%"
                                                                                                                        border="0"
                                                                                                                        cellspacing="0"
                                                                                                                        cellpadding="0">
                                                                                                                        <tbody>
                                                                                                                            <tr>
                                                                                                                                <td class="title-48 c-blue1 fw-b a-center"
                                                                                                                                    style="font-size:48px; line-height:52px; font-family:Arial, sans-serif, 'Motiva Sans'; color:#3a9aed; font-weight:bold; text-align:center;">
                                                                                                                                    {token}
                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                        </tbody>
                                                                                                                    </table>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
    """
    html_str3 = """
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="text-18 c-grey4 pb-30"
                                                                                                    style="font-size:18px; line-height:25px; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left; color:#dbdbdb; padding-bottom: 30px;">
                                                                                                    令牌验证码是完成注册所必需的，注册的邮箱将来会被用于密码找回。<span
                                                                                                        style="color: #ffffff; font-weight: bold;">请您在10分钟内完成验证，过时令牌作废。</span>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="text-18 c-blue1 pb-40"
                                                                                                    style="font-size:18px; line-height:25px; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left; color:#7abefa; padding-bottom: 40px;">
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>


                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="pt-30"
                                                                                                    style="padding-top: 30px;">
                                                                                                    <table width="100%"
                                                                                                        border="0"
                                                                                                        cellspacing="0"
                                                                                                        cellpadding="0">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td class="img"
                                                                                                                    width="3"
                                                                                                                    bgcolor="#3a9aed"
                                                                                                                    style="font-size:0pt; line-height:0pt; text-align:left;">
                                                                                                                </td>
                                                                                                                <td class="img"
                                                                                                                    width="37"
                                                                                                                    style="font-size:0pt; line-height:0pt; text-align:left;">
                                                                                                                </td>
                                                                                                                <td>
                                                                                                                    <table
                                                                                                                        width="100%"
                                                                                                                        border="0"
                                                                                                                        cellspacing="0"
                                                                                                                        cellpadding="0">
                                                                                                                        <tbody>
                                                                                                                            <tr>
                                                                                                                                <td class="text-16 py-20 c-grey4 fallback-font"
                                                                                                                                    style="font-size:16px; line-height:22px; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left; padding-top: 20px; padding-bottom: 20px; color:#f1f1f1;">
                                                                                                                                    祝您生活愉快，<br>
                                                                                                                                    CodeCheck团队
                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                        </tbody>
                                                                                                                    </table>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>


                                                                                </td>
                                                                            </tr>

                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>



                                                            <tr>
                                                                <td class="py-60 px-90 mpy-40 mpx-15"
                                                                    style="padding-top: 60px; padding-bottom: 60px; padding-left: 90px; padding-right: 90px;">
                                                                    <table width="100%" border="0" cellspacing="0"
                                                                        cellpadding="0">

                                                                        <tbody>
                                                                            <tr>
                                                                                <td class="text-18 pb-60 mpb-40 fallback-font"
                                                                                    style="font-size:18px; line-height:25px; color:#000001; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left; padding-bottom: 60px;">
                                                                                    此通知已发送至与您的 CodeCheck 帐户关联的电子邮件地址。
                                                                                    <br><br>
                                                                                    这封电子邮件由系统自动生成，请勿回复。 </td>
                                                                            </tr>


                                                                            <tr>
                                                                                <td class="pb-60"
                                                                                    style="padding-bottom: 60px;">
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <th class="column"
                                                                                                    width="270"
                                                                                                    style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
                                                                                                    <table width="100%"
                                                                                                        border="0"
                                                                                                        cellspacing="0"
                                                                                                        cellpadding="0">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td class="text-18 mpb-40 fallback-font"
                                                                                                                    style="font-size:18px; line-height:25px; color:#000001; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left;">
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </th>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>

                                                                           
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>

                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </center>

                <center
                    style="font-family:Arial, sans-serif, 'Motiva Sans'; color: #000000; font-size: 11px; margin-bottom: 4px;">
                    查看此消息时遇到问题？ <a
                        href="https://info.ruc.edu.cn"
                        style="font-family:Arial, sans-serif, 'Motiva Sans'; color: #000000; font-size: 11px; margin-bottom: 4px;"
                        rel="noopener" target="_blank">
                        点击此处 </a>
                </center>
                <style type="text/css">
                    .qmbox style,
                    .qmbox script,
                    .qmbox head,
                    .qmbox link,
                    .qmbox meta {
                        display: none !important;
                    }
                </style>
            </div>
        </div><!-- -->
        <style>
            #mailContentContainer .txt {
                height: auto;
            }
        </style>
    </div>
</body>

</html>
    """
    return html_str1+html_str2+html_str3


def getChangePasswdEmail(userName: str, token: str):
    html_str1 = """
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div id="contentDiv" onmouseover="getTop().stopPropagation(event);"
        onclick="getTop().preSwapLink(event, 'html', 'ZC0025_DQbNu8yM1LYu1GQA0GRhvd6');"
        style="position:relative;font-size:14px;height:auto;padding:15px 15px 10px 15px;z-index:1;zoom:1;line-height:1.7;"
        class="body">
        <div id="qm_con_body">
            <div id="mailContentContainer" class="qmbox qm_con_body_content qqmail_webmail_only" style="opacity: 1;">
                <style type="text/css" media="screen">
                    @font-face {
                        font-family: 'Motiva Sans';
                        font-style: normal;
                        font-weight: 300;
                        src: local('Motiva Sans'), url('https://store.akamai.steamstatic.com/public/shared/fonts/email/MotivaSans-Light.woff') format('woff');
                    }

                    @font-face {
                        font-family: 'Motiva Sans';
                        font-style: normal;
                        font-weight: normal;
                        src: local('Motiva Sans'), url('https://store.akamai.steamstatic.com//public/shared/fonts/email/MotivaSans-Regular.woff') format('woff');
                    }

                    @font-face {
                        font-family: 'Motiva Sans';
                        font-style: normal;
                        font-weight: bold;
                        src: local('Motiva Sans'), url('https://store.akamai.steamstatic.com//public/shared/fonts/email/MotivaSans-Bold.woff') format('woff');
                    }

                    .qmbox [style*='Motiva Sans'] {
                        font-family: 'Motiva Sans', Arial, sans-serif !important;
                    }
                </style>
                <style type="text/css" media="screen">
                    .qmbox body {
                        padding: 0 !important;
                        margin: 0 auto !important;
                        display: block !important;
                        min-width: 100% !important;
                        width: 100% !important;
                        background: #ffffff;
                        -webkit-text-size-adjust: none;
                    }

                    .qmbox a {
                        color: #7abefa;
                        text-decoration: underline;
                    }

                    .qmbox body a {
                        color: #ffffff;
                        text-decoration: underline;
                    }

                    .qmbox img {
                        margin: 0 !important;
                        -ms-interpolation-mode: bicubic;
                        /* Allow smoother rendering of resized image in Internet Explorer */
                    }

                    /* for recepits */
                    .qmbox table {
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                    }

                    .qmbox img,
                    .qmbox a img {
                        border: 0;
                        outline: none;
                        text-decoration: none;
                    }

                    .qmbox #outlook a {
                        padding: 0;
                    }

                    .qmbox .ReadMsgBody {
                        width: 100%;
                    }

                    .qmbox .ExternalClass {
                        width: 100%;
                    }

                    .qmbox div,
                    .qmbox p,
                    .qmbox a,
                    .qmbox li,
                    .qmbox td,
                    .qmbox blockquote {
                        mso-line-height-rule: exactly;
                    }

                    .qmbox a[href^=tel],
                    .qmbox a[href^=sms] {
                        color: inherit;
                        text-decoration: none;
                    }

                    .qmbox .ExternalClass,
                    .qmbox .ExternalClass p,
                    .qmbox .ExternalClass td,
                    .qmbox .ExternalClass div,
                    .qmbox .ExternalClass span,
                    .qmbox .ExternalClass font {
                        line-height: 100%;
                    }

                    /* END for recepits */

                    .qmbox a[x-apple-data-detectors] {
                        color: inherit !important;
                        text-decoration: inherit !important;
                        font-size: inherit !important;
                        font-family: inherit !important;
                        font-weight: inherit !important;
                        line-height: inherit !important;
                    }

                    .qmbox .btn-18 a {
                        display: block;
                        padding: 13px 35px;
                        text-decoration: none;
                    }

                    .qmbox .l-white a {
                        color: #ffffff;
                    }

                    .qmbox .l-black a {
                        color: #000001;
                    }

                    .qmbox .l-grey1 a {
                        color: #dbdee2;
                    }

                    .qmbox .l-grey2 a {
                        color: #a1a2a4;
                    }

                    .qmbox .l-grey3 a {
                        color: #dadcdd;
                    }

                    .qmbox .l-grey4 a {
                        color: #f1f1f1;
                    }

                    .qmbox .l-grey5 a {
                        color: #dddedf;
                    }

                    .qmbox .l-grey6 a {
                        color: #bfbfbf;
                    }

                    .qmbox .l-grey7 a {
                        color: #dcdddd;
                    }

                    .qmbox .l-grey8 a {
                        color: #8e96a4;
                    }

                    .qmbox .l-green a {
                        color: #a4d007;
                    }

                    .qmbox .l-blue a {
                        color: #6a7c96;
                    }

                    .qmbox .l-blue1 a {
                        color: #7abefa;
                    }

                    .qmbox .l-blue2 a {
                        color: #9eb8cc;
                    }


                    /* Mobile styles */
                    @media only screen and (max-device-width: 480px),
                    only screen and (max-width: 480px) {
                        .qmbox .mpy-35 {
                            padding-top: 35px !important;
                            padding-bottom: 35px !important;
                        }

                        .qmbox .mpx-15 {
                            padding-left: 15px !important;
                            padding-right: 15px !important;
                        }

                        .qmbox .mpx-20 {
                            padding-left: 20px !important;
                            padding-right: 20px !important;
                        }

                        .qmbox .mpb-30 {
                            padding-bottom: 30px !important;
                        }

                        .qmbox .mpb-10 {
                            padding-bottom: 10px !important;
                        }

                        .qmbox .mpb-15 {
                            padding-bottom: 15px !important;
                        }

                        .qmbox .mpb-20 {
                            padding-bottom: 20px !important;
                        }

                        .qmbox .mpb-35 {
                            padding-bottom: 35px !important;
                        }

                        .qmbox .mpb-40 {
                            padding-bottom: 40px !important;
                        }

                        .qmbox .mpb-50 {
                            padding-bottom: 50px !important;
                        }

                        .qmbox .mpb-60 {
                            padding-bottom: 60px !important;
                        }

                        .qmbox .mpt-30 {
                            padding-top: 30px !important;
                        }

                        .qmbox .mpt-40 {
                            padding-top: 40px !important;
                        }

                        .qmbox .mpy-40 {
                            padding-top: 40px !important;
                            padding-bottom: 40px !important;
                        }

                        .qmbox .mpt-0 {
                            padding-top: 0px !important;
                        }

                        .qmbox .mpr-0 {
                            padding-right: 0px !important;
                        }

                        .qmbox .mfz-14 {
                            font-size: 14px !important;
                        }

                        .qmbox .mfz-28 {
                            font-size: 28px !important;
                        }

                        .qmbox .mfz-16 {
                            font-size: 16px !important;
                        }

                        .qmbox .mfz-24 {
                            font-size: 24px !important;
                        }

                        .qmbox .mlh-18 {
                            line-height: 18px !important;
                        }

                        .qmbox u+body .gwfw {
                            width: 100% !important;
                            width: 100vw !important;
                        }

                        .qmbox .td,
                        .qmbox .m-shell {
                            width: 100% !important;
                            min-width: 100% !important;
                        }

                        .qmbox .mt-left {
                            text-align: left !important;
                        }

                        .qmbox .mt-center {
                            text-align: center !important;
                        }

                        .qmbox .mt-right {
                            text-align: right !important;
                        }

                        .qmbox .m-left {
                            text-align: left !important;
                        }

                        .qmbox .me-left {
                            margin-right: auto !important;
                        }

                        .qmbox .me-center {
                            margin: 0 auto !important;
                        }

                        .qmbox .me-right {
                            margin-left: auto !important;
                        }

                        .qmbox .mh-auto {
                            height: auto !important;
                        }

                        .qmbox .mw-auto {
                            width: auto !important;
                        }

                        .qmbox .fluid-img img {
                            width: 100% !important;
                            max-width: 100% !important;
                            height: auto !important;
                        }

                        .qmbox .column,
                        .qmbox .column-top,
                        .qmbox .column-dir,
                        .qmbox .column-dir-top {
                            float: left !important;
                            width: 100% !important;
                            display: block !important;
                        }

                        .qmbox .kmMobileStretch {
                            float: left !important;
                            width: 100% !important;
                            display: block !important;
                            padding-left: 0 !important;
                            padding-right: 0 !important;
                        }

                        .qmbox .m-hide {
                            display: none !important;
                            width: 0 !important;
                            height: 0 !important;
                            font-size: 0 !important;
                            line-height: 0 !important;
                            min-height: 0 !important;
                        }

                        .qmbox .m-block {
                            display: block !important;
                        }

                        .qmbox .mw-15 {
                            width: 15px !important;
                        }

                        .qmbox .mw-2p {
                            width: 2% !important;
                        }

                        .qmbox .mw-32p {
                            width: 32% !important;
                        }

                        .qmbox .mw-49p {
                            width: 49% !important;
                        }

                        .qmbox .mw-50p {
                            width: 50% !important;
                        }

                        .qmbox .mw-100p {
                            width: 100% !important;
                        }

                        .qmbox .mbgs-200p {
                            background-size: 200% auto !important;
                        }
                    }
                </style>
                <center>
                    <table width="100%" border="0" cellspacing="0" cellpadding="0"
                        style="margin: 0; padding: 0; width: 100%; height: 100%;" bgcolor="#ffffff" class="gwfw">
                        <tbody>
                            <tr>
                                <td style="margin: 0; padding: 0; width: 100%; height: 100%;" align="center"
                                    valign="top">
                                    <table width="775" border="0" cellspacing="0" cellpadding="0" class="m-shell">
                                        <tbody>
                                            <tr>
                                                <td class="td"
                                                    style="width:775px; min-width:775px; font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">

                                                        <tbody>
                                                            <tr>
                                                                <td class="p-80 mpy-35 mpx-15" bgcolor="#212429"
                                                                    style="padding: 80px;">
                                                                    <table width="100%" border="0" cellspacing="0"
                                                                        cellpadding="0">


                                                                        <tbody>
                                                                            <tr>
                                                                                <td class="img pb-45"
                                                                                    style="font-size:0pt; line-height:0pt; text-align:left; padding-bottom: 45px;">
                                                                                    <a href="https://info.ruc.edu.cn/"
                                                                                        target="_blank" rel="noopener">
                                                                                        <!-- <img src="http://info.ruc.edu.cn/images/logo.png"
                                                                                            width="265" height="88"
                                                                                            border="0"> -->
                                                                                    </a>

                                                                                </td>
                                                                            </tr>
    """

    html_str2 = f"""
                                                                            <tr>
                                                                                <td>
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="title-36 pb-30 c-grey6 fw-b"
                                                                                                    style="font-size:36px; line-height:42px; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left; padding-bottom: 30px; color:#bfbfbf; font-weight:bold;">
                                                                                                    {userName}，您好！</td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="text-18 c-grey4 pb-30"
                                                                                                    style="font-size:18px; line-height:25px; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left; color:#dbdbdb; padding-bottom: 30px;">
                                                                                                    您找回密码的帐户 {userName} 所需的令牌验证码为：</td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="pb-70 mpb-50"
                                                                                                    style="padding-bottom: 70px;">
                                                                                                    <table width="100%"
                                                                                                        border="0"
                                                                                                        cellspacing="0"
                                                                                                        cellpadding="0"
                                                                                                        bgcolor="#17191c">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td class="py-30 px-56"
                                                                                                                    style="padding-top: 30px; padding-bottom: 30px; padding-left: 56px; padding-right: 56px;">
                                                                                                                    <table
                                                                                                                        width="100%"
                                                                                                                        border="0"
                                                                                                                        cellspacing="0"
                                                                                                                        cellpadding="0">
                                                                                                                        <tbody>
                                                                                                                            <tr>
                                                                                                                                <td class="title-48 c-blue1 fw-b a-center"
                                                                                                                                    style="font-size:48px; line-height:52px; font-family:Arial, sans-serif, 'Motiva Sans'; color:#3a9aed; font-weight:bold; text-align:center;">
                                                                                                                                    {token}
                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                        </tbody>
                                                                                                                    </table>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
    """
    html_str3 = """
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="text-18 c-grey4 pb-30"
                                                                                                    style="font-size:18px; line-height:25px; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left; color:#dbdbdb; padding-bottom: 30px;">
                                                                                                    令牌验证码是完成密码找回所必需的，<span
                                                                                                        style="color: #ffffff; font-weight: bold;">请您在10分钟内完成验证，过时令牌作废。</span>
                                                                                                        如您遇到任何问题，请联系开发者。
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="text-18 c-blue1 pb-40"
                                                                                                    style="font-size:18px; line-height:25px; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left; color:#7abefa; padding-bottom: 40px;">
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>


                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td class="pt-30"
                                                                                                    style="padding-top: 30px;">
                                                                                                    <table width="100%"
                                                                                                        border="0"
                                                                                                        cellspacing="0"
                                                                                                        cellpadding="0">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td class="img"
                                                                                                                    width="3"
                                                                                                                    bgcolor="#3a9aed"
                                                                                                                    style="font-size:0pt; line-height:0pt; text-align:left;">
                                                                                                                </td>
                                                                                                                <td class="img"
                                                                                                                    width="37"
                                                                                                                    style="font-size:0pt; line-height:0pt; text-align:left;">
                                                                                                                </td>
                                                                                                                <td>
                                                                                                                    <table
                                                                                                                        width="100%"
                                                                                                                        border="0"
                                                                                                                        cellspacing="0"
                                                                                                                        cellpadding="0">
                                                                                                                        <tbody>
                                                                                                                            <tr>
                                                                                                                                <td class="text-16 py-20 c-grey4 fallback-font"
                                                                                                                                    style="font-size:16px; line-height:22px; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left; padding-top: 20px; padding-bottom: 20px; color:#f1f1f1;">
                                                                                                                                    祝您生活愉快，<br>
                                                                                                                                    CodeCheck团队
                                                                                                                                </td>
                                                                                                                            </tr>
                                                                                                                        </tbody>
                                                                                                                    </table>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>


                                                                                </td>
                                                                            </tr>

                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>



                                                            <tr>
                                                                <td class="py-60 px-90 mpy-40 mpx-15"
                                                                    style="padding-top: 60px; padding-bottom: 60px; padding-left: 90px; padding-right: 90px;">
                                                                    <table width="100%" border="0" cellspacing="0"
                                                                        cellpadding="0">

                                                                        <tbody>
                                                                            <tr>
                                                                                <td class="text-18 pb-60 mpb-40 fallback-font"
                                                                                    style="font-size:18px; line-height:25px; color:#000001; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left; padding-bottom: 60px;">
                                                                                    此通知已发送至与您的 CodeCheck 帐户关联的电子邮件地址。
                                                                                    <br><br>
                                                                                    这封电子邮件由系统自动生成，请勿回复。 </td>
                                                                            </tr>


                                                                            <tr>
                                                                                <td class="pb-60"
                                                                                    style="padding-bottom: 60px;">
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <th class="column"
                                                                                                    width="270"
                                                                                                    style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
                                                                                                    <table width="100%"
                                                                                                        border="0"
                                                                                                        cellspacing="0"
                                                                                                        cellpadding="0">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td class="text-18 mpb-40 fallback-font"
                                                                                                                    style="font-size:18px; line-height:25px; color:#000001; font-family:Arial, sans-serif, 'Motiva Sans'; text-align:left;">
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </th>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>


                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>

                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </center>

                <center
                    style="font-family:Arial, sans-serif, 'Motiva Sans'; color: #000000; font-size: 11px; margin-bottom: 4px;">
                    查看此消息时遇到问题？ <a
                        href="https://info.ruc.edu.cn"
                        style="font-family:Arial, sans-serif, 'Motiva Sans'; color: #000000; font-size: 11px; margin-bottom: 4px;"
                        rel="noopener" target="_blank">
                        点击此处 </a>
                </center>
                <style type="text/css">
                    .qmbox style,
                    .qmbox script,
                    .qmbox head,
                    .qmbox link,
                    .qmbox meta {
                        display: none !important;
                    }
                </style>
            </div>
        </div><!-- -->
        <style>
            #mailContentContainer .txt {
                height: auto;
            }
        </style>
    </div>
</body>

</html>
    """
    return html_str1 + html_str2 + html_str3