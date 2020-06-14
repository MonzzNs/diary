function addEvent(node, type, callback) {
    if (node.addEventListener) {
        node.addEventListener(type, function (e) {
            callback(e, e.target);
        }, false);
    } else if (node.attachEvent) {
        node.attachEvent('on' + type, function (e) {
            callback(e, e.srcElement);
        });
    }
}

function registerValidator(field) {
    return (
        !(field.getAttribute("readonly") || field.readonly) &&
        !(field.getAttribute("disabled") || field.disabled) &&
        (field.getAttribute("pattern") || field.getAttribute("required"))
    );
}