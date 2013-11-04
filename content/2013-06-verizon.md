Title: Verizon Doesn't Want My Money
Date: 2013-06-16 21:47
Tags: fail, javascript, verizon

I was trying to upgrade my dad's phone the other day, from an old iPhone 4 to a S3. I went on Verizon, picked the phone, picked the plan, and was ready to check out when I got to the billing page.

[![Verizon Sucks]({filename}/images/verizon1.png)]({filename}/images/verizon1.png)

### Wait, what?

Something seems to be missing here. How do I get to the next page? I refreshed the page a few times and it was still missing. Naturally, I  opened up the developer console and looked at the source. I found the form element, the inputs for all the credit card info and the customer agreement, but no submit or button of any sort. They weren't hidden, they simply didn't exist. What I did find, however, was a Javascript error:

    :::text
    TypeError: Cannot call method 'init' of undefined

And here is the relevant code:

    :::javascript
    $j(function() {
        $j("#billingForm").validateForm({
            postNoticeAdjacent:true,
            highlightInvalidFields:true,
            realTimeValidation:true,
            callback:function(){
                //If there's a credit card number. Validate the other CC fields as required
                var ccNumField = $j("#p_cc_num");
                ccFields = $j("#debitCard").find(":input:not([readonly]):not([disabled])");
                if(!this.isEmpty(ccNumField)) {
                    if(!vz.ui.cc.verifyCard(ccNumField.val())) {
                        this.markField(ccNumField);
                        this.invalid = true;
                    }
                    var self = this;
                    ccFields.prop("required",true);
                    ccFields.each(function() {
                        self.validate(this);
                    });
                    ccFields.prop("required",false);
                }
                if(!this.invalid && doContinue()) {
                    return true;
                } else {
                    return false;
                }
            }
        });
        vz.ui.cc.init();
    });

The first thing I noticed was that it had comments and wasn't minified. I expected better out of the production website of our nation's largest mobile provider. I dug around the source code some more. Here's another snippet I found:

    :::javascript
    function hide()
    {
     
            /*$j('#td_GCPlus').css('display', 'block');
            $j('#giftCard').css('display', 'none');*/
            Toggle('GC');
     
    }

More commented, un-minified production code. Really?

    :::javascript
    function disableCCGC(chckbxSt){
        if(document.getElementById('creditCard').style.display=='block'){
            document.billingForm.p_cc_type.disabled=chckbxSt;
            document.getElementById('p_cc_num').disabled=chckbxSt;
            document.getElementById('p_cc_exp_month').disabled=chckbxSt;
            document.getElementById('p_cc_exp_year').disabled=chckbxSt;
            document.getElementById('p_cc_exp_year').disabled=chckbxSt;
            document.getElementById('p_cc_exp_year').disabled=chckbxSt;
            document.getElementById('p_cvn').disabled=chckbxSt;
            document.getElementById('p_zipcode').disabled=chckbxSt;
        }
     
        if(document.getElementById('giftCard').style.display=='block'){
            document.getElementById('giftCardNumber1').disabled=chckbxSt;
            document.getElementById('giftCardPin1').disabled=chckbxSt;
            document.getElementById('giftCardNumber2').disabled=chckbxSt;
            document.getElementById('giftCardPin2').disabled=chckbxSt;
        }
    }
     
    function clearCCGC(){
        document.billingForm.p_cc_type.value="";
        document.getElementById('p_cc_num').value="";
        document.getElementById('p_cc_exp_month').value="";
        document.getElementById('p_cc_exp_year').value="";
        document.getElementById('p_cc_exp_year').value="";
        document.getElementById('p_cc_exp_year').value="";
        document.getElementById('p_cvn').value="";
        document.getElementById('p_zipcode').value="";
     
        document.getElementById('giftCardNumber1').value="";
        document.getElementById('giftCardPin1').value="";
     
        document.getElementById('giftCardNumber2').value="";
        document.getElementById('giftCardPin2').value="";
    }

Here we see that they prefer to manipulate the DOM directly, even though they're already using MooTools. They also query for elements every time as opposed to caching them in variables. Amateurs.

    :::javascript
    var x;
    var ccDetails = new Array();
    ccDetails[0]=document.billingForm.p_cc_type;
    ccDetails[1]=document.getElementById('p_cc_num');
    ccDetails[2]=document.getElementById('p_cc_exp_month');
    ccDetails[3]=document.getElementById('p_cc_exp_year');
    ccDetails[4]=document.getElementById('p_cvn');
    ccDetails[5]=document.getElementById('p_zipcode');
    for (x in ccDetails){
        if(!IsEmpty(ccDetails[x])){
            if(document.getElementById('creditCard').style.display=='none')
                //Toggle('CC');
            break;
        }
    }
    var y;
    var gcDetails = new Array();
    gcDetails[0]=document.getElementById('giftCardNumber1');
    gcDetails[1]=document.getElementById('giftCardPin1');
     
    gcDetails[2]=document.getElementById('giftCardNumber2');
    gcDetails[3]=document.getElementById('giftCardPin2');
     
    for (y in gcDetails){
        if(!IsEmpty(gcDetails[y])){
            if(document.getElementById('giftCard').style.display=='none')
                Toggle('GC');
            break;
        }
    }

Again, more inefficient DOM querying. Here they're also using `for ... in` to iterate over the array, which can cause problems.

    :::html
    <script type="text/javascript">
    //5050 = 'groupB';
    //campaign = '';
    //recipe = '';
    </script>

This script here accomplishes... absolutely nothing. Ok.

With all this absolutely awful Javascript, it's no wonder that a bug like "not having a continue button" could exist. The error seemed to be that the credit card module wasn't imported or defined correctly. If I really, really wanted to finish that page, I could have added a submit button myself and submitted the form. But that might just cause Verizon to accidentally charge me 50 times, which they would have gladly done. In the end, I gave up on the web site, went back to the 1880s, and did the upgrade by phone. Had I been shopping for a new carrier, this error would have completely prevented me from signing up with Verizon. This is a critical bug, and another reason why Verizon sucks.
