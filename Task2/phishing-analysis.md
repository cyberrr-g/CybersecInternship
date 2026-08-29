# Task 2: Phishing Email Analysis

## 1. Objective

The objective of this task is to identify common phishing
characteristics in a suspicious email sample and understand how
attackers use social engineering, spoofing, suspicious links, and urgent
language to deceive users.

## 2. Tools Used

-   Kali Linux
-   Email sample (safe simulated phishing email)
-   Email header analysis concepts
-   Web browser for research
-   Text editor



> **Note:** This is a safe simulated phishing email created for
> educational analysis. It does not contain a real malicious URL or
> credential-collection page.

## 4. Sender Analysis

The email claims to come from the Microsoft Account Security Team, but
the sender address uses:

`security-alert@email.com`


**Finding:** Suspicious sender/domain and wrong email address.

## 5. Email Header Analysis

A real phishing investigation should examine the raw email headers,
including:

-   From
-   Return-Path
-   Received
-   Message-ID
-   SPF


**Finding:** Header analysis could not be performed because this is a
simulated sample without real delivery headers.

## 6. Suspicious Links and Attachments

The email contains a verification call-to-action:

`[http://microsof.security-alert/amannn/login/crenditials]`

The sample does not contain an actual URL. Therefore, the real
destination cannot be checked and no URL mismatch should be claimed.


**Finding:** The email attempts to persuade the recipient to use an
account-verification link, but no real link or attachment is included in
this safe sample.

## 7. Urgent and Threatening Language

The email uses several pressure techniques:

-   `URGENT` in the subject
-   "within 24 hours"
-   "account may be temporarily restricted"
-   "access ... may be suspended"

**Finding:** Urgency and threats are major phishing indicators.


## 8. Spelling and Grammar Analysis

The absence of grammar errors does not mean that an email is legitimate.
Phishing emails can be professionally written and still be malicious.

**Finding:** The sample contain obvious spelling or grammar mistakes..


## 9. Overall Assessment

The email shows multiple characteristics associated with phishing:

-   It impersonates a trusted organization.
-   The sender domain is suspicious.
-   It uses urgent language.
-   It creates fear by threatening account restrictions.
-   It asks the recipient to verify an account.
-   It uses social-engineering techniques to encourage immediate action.

Because the sample is simulated, it does not contain real delivery
headers or a real malicious URL. Therefore, those technical indicators
cannot be verified.

## 10. Conclusion

The sample should be treated as a phishing-style email because it uses
impersonation, urgency, threats, and an account-verification request to
influence the recipient.

A user receiving a similar real-world email should avoid clicking links
or opening unexpected attachments and should verify the request through
the organization's official website or another trusted communication
channel.

