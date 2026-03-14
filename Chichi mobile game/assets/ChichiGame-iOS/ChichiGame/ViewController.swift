import UIKit
import WebKit

class ViewController: UIViewController, WKNavigationDelegate, WKUIDelegate {

    private var webView: WKWebView!

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .black

        let config = WKWebViewConfiguration()
        config.allowsInlineMediaPlayback = true
        config.mediaTypesRequiringUserActionForPlayback = []
        config.preferences.setValue(true, forKey: "allowFileAccessFromFileURLs")

        webView = WKWebView(frame: .zero, configuration: config)
        webView.navigationDelegate = self
        webView.uiDelegate = self
        webView.scrollView.isScrollEnabled = false
        webView.scrollView.bounces = false
        webView.scrollView.contentInsetAdjustmentBehavior = .never
        webView.isOpaque = false
        webView.backgroundColor = .black
        webView.translatesAutoresizingMaskIntoConstraints = false

        view.addSubview(webView)
        NSLayoutConstraint.activate([
            webView.topAnchor.constraint(equalTo: view.topAnchor),
            webView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            webView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            webView.trailingAnchor.constraint(equalTo: view.trailingAnchor)
        ])

        guard let webDir = Bundle.main.url(forResource: "web", withExtension: nil),
              let indexURL = URL(string: webDir.absoluteString + "/index.html") else { return }
        webView.loadFileURL(indexURL, allowingReadAccessTo: webDir)
    }

    // Unlock Web Audio API on first touch (iOS requirement)
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        webView.evaluateJavaScript("""
        (function(){
          var _unlocked=false;
          document.addEventListener('touchstart',function _u(){
            if(_unlocked)return; _unlocked=true;
            var A=window.AudioContext||window.webkitAudioContext;
            if(A){var c=new A();c.resume().then(function(){c.close()});}
            document.removeEventListener('touchstart',_u);
          },{passive:true});
        })();
        """, completionHandler: nil)
    }

    // Safe area insets via JS so CSS can use them
    override func viewSafeAreaInsetsDidChange() {
        super.viewSafeAreaInsetsDidChange()
        let i = view.safeAreaInsets
        let js = "document.documentElement.style.setProperty('--sat','\(i.top)px');"
                + "document.documentElement.style.setProperty('--sab','\(i.bottom)px');"
                + "document.documentElement.style.setProperty('--sal','\(i.left)px');"
                + "document.documentElement.style.setProperty('--sar','\(i.right)px');"
        webView.evaluateJavaScript(js, completionHandler: nil)
    }

    override var prefersStatusBarHidden: Bool { true }
    override var supportedInterfaceOrientations: UIInterfaceOrientationMask { .portrait }
    override var preferredScreenEdgesDeferringSystemGestures: UIRectEdge { .all }
}
