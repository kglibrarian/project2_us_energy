// SVGオブジェクト
var $svg;
// SVG読み込み
var loadSvgObject = function() {
    if (!$svg) {
        var svgTag = document.getElementById('svg-obj');
        if (!svgTag) return;
        var svgDoc = svgTag.contentDocument;
        $svg = $(svgDoc).find('svg');
    }
};

$(window).on('load', function() {
    // OK
    loadSvgObject();
    //...処理
});