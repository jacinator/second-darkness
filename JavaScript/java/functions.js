var classify = function(string) {
    return string.replace("_", "-")
                 .replace(" ", "-")
                 .toLowerCase();
};