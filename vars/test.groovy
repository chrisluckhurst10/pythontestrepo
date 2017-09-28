def call(String input) {

    def remoteUrl = scm.getUserRemoteConfigs()[0].getUrl()

	return remoteUrl
}
