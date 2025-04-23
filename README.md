# Copilot-Fix-For-Models-For-cline-roo-
Copilot Fix For Models For cline+roo to enable sonnent 3.7


# Remove `x-onbehalf-extension-id` Header from GitHub Copilot Chat Extension

This guide helps you remove the `x-onbehalf-extension-id` header from your GitHub Copilot Chat extension in VS Code.

> **Note:** Modifying extension files may cause your changes to be overwritten during updates. Always back up the file before making changes.

## Automatic Mode (Python Script)

You can use the provided Python script to automatically remove the header from `extension.js`:

1.  Download and run the Python script.
2.  The script will prompt you to select your `extension.js` file.
3.  It will automatically remove the `x-onbehalf-extension-id` header.

## Manual Mode

1.  Locate `extension.js` inside the `github.copilot-chat-<version>/dist` folder.
2.  Open the file and search for:
    ```plaintext
    "x-onbehalf-extension-id"
    ```
3.  Remove or comment out the line:
    ```javascript
    headers["x-onbehalf-extension-id"] = "some-value";
    ```

    **Example:**
    ```javascript
    // headers["x-onbehalf-extension-id"] = "some-value";
    ```
4.  Save the file and restart VS Code.
