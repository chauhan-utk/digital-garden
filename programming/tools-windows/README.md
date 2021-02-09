# Tools - Windows

{% tabs %}
{% tab title="Terminal App" %}
Available on Windows Store \(as of December 2020\).

To add Anaconda Prompt specific environment in the shortcut, add following block in `settings.json`

```javascript
{
// Make changes here to the cmd.exe profile.
"guid": "{61b63770-307b-4a4c-a433-9c8340e5b36c}", // add another GUID
"name": "Anaconda",
"commandline": "cmd.exe /K %USERPROFILE%\\AppData\\Local\\Continuum\\anaconda3\\Scripts\\activate.bat %USERPROFILE%\\AppData\\Local\\Continuum\\anaconda3\\envs\\<env-name>",
"icon": "%USERPROFILE%\\AppData\\Local\\Continuum\\anaconda3\\Menu\\Iconleak-Atrous-PSConsole.ico",
"hidden": false
}
```

To make it as default, provide the guid in `defaultProfile`

```text
"defaultProfile": "{61b63770-307b-4a4c-a433-9c8340e5b36c}"
```
{% endtab %}

{% tab title="WSL" %}
#### What is WSL?

 The [**Windows Subsystem for Linux \(WSL\)**](https://www.tenforums.com/tutorials/46769-enable-disable-windows-subsystem-linux-windows-10-a.html) is a new **Windows 10** feature that enables you to run native Linux command-line tools directly on Windows, alongside your traditional Windows desktop and modern store apps. \(yay!\)

There's new WSL2 now \(as of December 2020\). Why that's relevant? To quote other awesome developer [from](https://www.digitalocean.com/community/posts/trying-the-new-wsl-2-its-fast-windows-subsystem-for-linux)

> I haven’t done any exhaustive, scientific, or precise tests by any means. What I have found though is that WSL is about **5 times faster for everyday web development tasks like npm or yarn.**

**How to \(uninstall WSL1\) install WSL2?**

Refer this article: [https://www.digitalocean.com/community/posts/trying-the-new-wsl-2-its-fast-windows-subsystem-for-linux](https://www.digitalocean.com/community/posts/trying-the-new-wsl-2-its-fast-windows-subsystem-for-linux)

#### Moving to another drive

[https://github.com/MicrosoftDocs/WSL/issues/412](https://github.com/MicrosoftDocs/WSL/issues/412)
{% endtab %}
{% endtabs %}







