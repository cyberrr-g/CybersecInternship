# Task 6: Create a Strong Password and Evaluate Its Strength

## Objective
Understand what makes a password strong, test passwords of varying complexity on a password strength checker (passwordmeter.com), and note best practices.

---

## 1. Test Passwords & Results

| Password | Length | Character Mix | Score | Rating |
|---|---|---|---|---|
| `password` | 8 | lowercase only | 5–10 | Very Weak — common word |
| `qwertyuiop` | 10 | lowercase, keyboard pattern | 5–15 | Very Weak — sequential pattern |
| `Password1` | 10 | upper+lower+number | 35–45 | Weak — predictable pattern |
| `P@ssword1` | 9 | upper+lower+number+symbol | 45–55 | Medium — known substitution trick |
| `Xk9#mQ2!vL` | 10 | fully random, all 4 types | 75–85 | Strong |
| `G7$pL9#zR4@wQ1` | 14 | fully random, all 4 types | 90–95 | Very Strong |
| `correct-horse-battery-staple` | 29 | lowercase passphrase | 90–100 | Very Strong |

**Key observation:** Length beats cleverness — a long lowercase passphrase scored as high as a short fully-random string. Dictionary words and keyboard patterns score lowest regardless of length.

---

## 2. Best Practices

- **Length matters most** — use 12–16+ characters
- Mix uppercase, lowercase, numbers, symbols when possible
- Avoid dictionary words, names, keyboard patterns (`qwerty`, `12345`)
- Avoid obvious substitutions (`@` for `a`, `0` for `o`) — attackers already check these
- Never reuse passwords across accounts
- Use a password manager to generate/store unique passwords
- Enable multi-factor authentication (MFA)
- Consider random-word passphrases (easy to remember, hard to crack)

---

## 3. Common Password Attacks

1. **Credential stuffing** — reused breached passwords tried across other sites
2. **Dictionary attacks** — common words/names + mutations (leetspeak, added digits)
3. **Pattern matching** — keyboard walks, sequences, dates
4. **Brute force** — tries every combination; only used once other methods fail; fast on short/simple passwords

---

## 4. How Complexity Affects Security

- Entropy grows **exponentially** with length: H = L x log2(N)
- One extra character in a 95-symbol set multiplies guesses by 95x
- Composition rules matter less than length once a password is unpredictable (per current NIST SP 800-63B guidance)
- Predictable "complex" passwords (e.g., `P@ssword1`) are still weak — real cracking tools check these patterns first

---

## Conclusion
Length + randomness (or a long passphrase) + uniqueness + MFA = the strongest practical defense against real-world password attacks.

*Note: All test passwords are examples only, not real credentials.*
