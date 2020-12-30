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

{% tab title="Second Tab" %}

{% endtab %}
{% endtabs %}



