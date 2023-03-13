class zh_cn:
    def __init__(self):
        self.ErrorRetrievingConfig = "获取配置失败"
        self.launch = "启动AppleID_Auto"
        self.failOnPasswordUpdate = "更新密码失败"
        self.failOnRetrievingPassword = "获取密码失败"
        self.failOnMessageUpdate = "更新消息失败"
        self.failOnReportingProxyError = "上报代理错误失败"
        self.failOnRetrievingProxyFromAPI = "从API获取代理失败"
        self.retrievedProxyFromAPI = "从API获取到代理"
        self.backgroundRunning = "已启用 后台运行"
        self.removeDevice = "已启用 删除设备"
        self.checkPassword = "已启用 检查密码"
        self.autoUpdatePassword = "已启用 定时更新密码"
        self.usingProxyID = "使用代理ID"
        self.failOnRefreshingPage = "刷新页面失败"
        self.proxyEnabledRefreshing = "已启用代理，请检查代理是否可用"
        self.proxyEnabledRefreshingAPI = "页面加载失败，可能是代理不可用"
        self.failOnLoadingPage = "页面加载失败"
        self.IPBlocked = "页面加载失败，疑似服务器IP被封禁"
        self.seeLog = "页面加载失败，具体原因请查看日志"
        self.failOnGettingCaptcha = "无法获取验证码"
        self.failOnRetrievingPage = "无法获取页面内容，即将退出程序"
        self.proxyEnabledGettingContent = "无法获取页面内容，可能是代理不可用"
        self.failOnGettingPage = "无法获取页面内容"
        self.captchaCorrect = "验证码正确"
        self.captchaFail = "验证码错误，重新输入"
        self.login = "登录成功"
        self.blocked = "无法处理请求，可能是账号失效或服务器IP被拉黑"
        self.loginFailCheckLog = "解锁登录失败，可能是账号失效或服务器IP被拉黑，具体请查看后端日志"
        self.notLocked = "当前账号未被锁定"
        self.locked = "当前账号已被锁定"
        self.twoStepnotEnabled = "当前账号未开启2FA"
        self.twoStepEnabled = "当前账号已开启2FA"
        self.cantFindDisable2FA = "关闭二步验证失败，可能是账号不允许关闭2FA"
        self.rejectedByApple = "操作被苹果拒绝，疑似被风控"
        self.chooseFail = "选择选项失败，无法使用安全问题解锁"
        self.loginLoadFail = "登录页面加载失败"
        self.answerIncorrect = "安全问题错误，程序已退出"
        self.answerNotMatch = "未找到安全问题对应答案，请检查配置"
        self.failOnBypass2FA = "跳过双重验证失败"
        self.startRemoving = "开始删除设备"
        self.noRemoveRequired = "没有设备需要删除"
        self.finishRemoving = "设备删除完毕"
        self.DOB_Error = "安全问题获取失败，可能是生日错误"
        self.failOnAnswer = "安全问题答案错误"
        self.passwordNotFound = "密码框获取失败"
        self.unknownError = "疑似密码修改失败？看到此报错请与作者反馈。已保存错误信息至日志"
        self.passwordUpdated = "密码修改成功，新密码为"
        self.startChangePassword = "开始修改密码"
        self.failOnChangePassword = "现在无法修改密码，可能是二步验证关闭失败"
        self.failToUseSecurityQuestion = "无法使用安全问题重设密码，修改失败"
        self.TGFail = "Telegram发送消息失败"
        self.cnTG = "如果机器在中国大陆，请勿开启Telegram通知"
        self.failOnCallingWD = "Webdriver调用失败"
        self.twoStepDetected = "检测到账号开启双重认证，开始解锁"
        self.accountLocked = "检测到账号被锁定，开始解锁"
        self.updateSuccess = "Apple ID更新成功"
        self.newPassword = "新密码: "
        self.passwordChanged = "密码错误，开始修改密码"
        self.LoginFail = "登录Apple ID失败，无法删除设备"
        self.missionFailed = "任务执行失败，等待下次检测"
        self.WDCloseError = "Webdriver关闭失败"
        self.repoAddress = "项目地址"
        self.TG_Group = "Telegram交流群"
        self.version = "当前版本"

class en_us:
    def __init__(self):
        self.ErrorRetrievingConfig = "Error retrieving config"
        self.launch = "Launch AppleID_Auto"
        self.failOnPasswordUpdate = "Password update failed"
        self.failOnRetrievingPassword = "Retrieving password failed"
        self.failOnMessageUpdate = "Message update failed"
        self.failOnReportingProxyError = "Reporting proxy error failed"
        self.failOnRetrievingProxyFromAPI = "Retrieving proxy from API failed"
        self.retrievedProxyFromAPI = "Retrieved proxy from API"
        self.backgroundRunning = "Background running enabled"
        self.removeDevice = "Remove device enabled"
        self.checkPassword = "Check password enabled"
        self.autoUpdatePassword = "Auto update password enabled"
        self.UsingProxyID = "Using proxy ID"
        self.failOnRefreshingPage = "Refreshing page failed"
        self.proxyEnabledRefreshing = "Proxy is enabled, please check the availability of proxy"
        self.proxyEnabledRefreshingAPI = "Page loading failed, proxy may not be available"
        self.failOnLoadingPage = "Page loading failed"
        self.IPBlocked = "Page loading failed, the server IP may be blocked"
        self.seeLog = "Page loading failed, please check the log for details"
        self.failOnGettingCaptcha = "Failed to get captcha"
        self.failOnRetrievingPage = "Failed to retrieve page content, exiting"
        self.proxyEnabledGettingContent = "Failed to retrieve page content, proxy may not be available"
        self.failOnGettingPage = "Failed to retrieve page content"
        self.captchaCorrect = "Captcha correct"
        self.captchaFail = "Captcha incorrect, please try again"
        self.login = "Login successful"
        self.blocked = "Unable to process request, account may be invalid or server IP may be blocked"
        self.loginFailCheckLog = "Login failed, account may be invalid or server IP may be blocked, " \
                                 "please check the backend log for details"
        self.notLocked = "Account is not locked"
        self.locked = "Account is locked"
        self.twoStepnotEnabled = "2FA is not enabled"
        self.twoStepEnabled = "2FA is enabled"
        self.cantFindDisable2FA = "Failed to disable 2FA, account may not allow 2FA to be disabled"
        self.rejectedByApple = "Action rejected by Apple, suspected of being under risk control"
        self.chooseFail = "Failed to choose option, unable to unlock by security questions"
        self.loginLoadFail = "Login page loading failed"
        self.answerIncorrect = "Security question answer incorrect, program exited"
        self.answerNotMatch = "Answers for security questions not found, please check the config"
        self.failOnBypass2FA = "Failed to bypass 2FA"
        self.startRemoving = "Start removing device"
        self.noRemoveRequired = "No device to remove"
        self.finishRemoving = "Device removal complete"
        self.DOB_Error = "Failed to get security question, birthday may be incorrect"
        self.failOnAnswer = "Security question answer incorrect"
        self.passwordNotFound = "Password box not found"
        self.unknownError = "Password may not be changed? If you see this error, please contact the author. " \
                            "Error information has been saved to the log"
        self.passwordUpdated = "Password updated, new password is "
        self.startChangePassword = "Start changing password"
        self.failOnChangePassword = "Unable to change password now, 2FA may not be disabled"
        self.failToUseSecurityQuestion = "Unable to use security question to reset password, password change failed"
        self.TGFail = "Telegram message sending failed"
        self.cnTG = "If your server is located in mainland China, please do not enable Telegram notification"
        self.failOnCallingWD = "Webdriver calling failed"
        self.twoStepDetected = "2FA is enabled, start unlocking"
        self.accountLocked = "Account is locked, start unlocking"
        self.updateSuccess = "Apple ID updated successfully"
        self.newPassword = "New password: "
        self.passwordChanged = "Password incorrect, start changing password"
        self.LoginFail = "Login Apple ID failed, unable to remove device"
        self.missionFailed = "Mission failed, waiting for next check"
        self.WDCloseError = "Webdriver close failed"
        self.repoAddress = "Project repo address"
        self.TG_Group = "Telegram group"
        self.version = "Current version"
