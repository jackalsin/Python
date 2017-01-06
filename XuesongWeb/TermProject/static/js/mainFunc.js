function sendMemo() {
    var memoText = $("#memo-text").val();
    var memoPhone = $("#memo-phone").val();
    var memoEmail = $("#memo-email").val();
    var memoName = $("#memo-name").val();
    if (memoText && memoName && /.+@.+\..+/.test(memoEmail) && /\d{3}-?\d{3}-?\d{4}/.test(memoPhone)) {
        // send Http
        if (memoText.length > 140) {
            alert("text length cannot be over 140 characters")
        } else if (memoName.length> 25) {
            alert("name length cannot be over 25 characters");
        } else {
            $.ajax({url:"/addmemo/?phone=" + memoPhone + "&text="+memoText+"&name="+memoName+"&email="+memoEmail,
            success: function (result) {
                if (result == "Succeed") {
                    alert("Succeed");
                    $("#memo-text").val("");
                    $("#memo-phone").val("");
                    $("#memo-email").val("");
                    $("#memo-name").val("");
                } else {
                    alert("Please submit latter.")
                }
            }
        });
        }
    } else {
        alert("Please enter valid value");
    }
}