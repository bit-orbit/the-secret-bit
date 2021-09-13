function checkRtl( character ) {
    var RTL = ['ا','ب','پ','ت','س','ج','چ','ح','خ','د','ذ','ر','ز','ژ','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ک','گ','ل','م','ن','و','ه','ی'];
    return RTL.indexOf( character ) > -1;
};

var divs = document.getElementsByTagName( 'p' );

for ( var index = 0; index < divs.length; index++ ) {
    if( checkRtl( divs[index].textContent[0] ) ) {
        divs[index].className = 'rtl';
    } else {
        divs[index].className = 'ltr';
    };
};