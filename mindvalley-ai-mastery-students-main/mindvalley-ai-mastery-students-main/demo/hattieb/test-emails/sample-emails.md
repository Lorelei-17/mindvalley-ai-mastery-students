# Hattie B's Test Email Scenarios

**Purpose**: Realistic customer emails testing all aspects of the email response system.

**How to Use**: Copy email body into test system. Check that routing, response quality, and QA evaluation match expectations.

---

## 1. Heat Level Question (Easy - Positive)

**From**: Jessica Martinez <jmartinez@gmail.com>
**Subject**: First time visitor - heat level help?

**Email Body**:
```
Hi there!

I'm visiting Nashville next week and HAVE to try Hattie B's based on all the hype. But I'm a little nervous about the spice levels - I like hot food but don't want to cry into my chicken lol.

What heat level would you recommend for someone who handles jalapeños fine but has never done a real Nashville hot chicken experience?

Thanks!
Jessica
```

**Expected Routing**:
- **CinnaMon**: Positive/neutral sentiment → route to normal flow
- **Hatch**: Retrieves heat level guide from KB
- **YGM**: Drafts helpful recommendation (likely Damn Hot or Hot)
- **QA**: Should PASS - straightforward question with KB answer

**Expected Outcome**: SHIP

**QA Checkpoints**:
- [ ] Specific heat level recommended
- [ ] Explains why that level fits their tolerance
- [ ] Warm, welcoming tone
- [ ] Mentions ability to customize
- [ ] No hallucinated menu items

---

## 2. Location & Hours (Easy - Neutral)

**From**: David Chen <dchen82@yahoo.com>
**Subject**: Nashville locations

**Email Body**:
```
Do you have multiple locations in Nashville? What are the hours for the midtown location?

Thanks
David
```

**Expected Routing**:
- **CinnaMon**: Neutral sentiment → normal flow
- **Hatch**: Retrieves location/hours info from KB
- **YGM**: Drafts factual response
- **QA**: Should PASS - factual KB lookup

**Expected Outcome**: SHIP

**QA Checkpoints**:
- [ ] Lists all Nashville locations
- [ ] Provides accurate hours
- [ ] Mentions wait times or best times to visit
- [ ] Professional but friendly tone
- [ ] No made-up locations

---

## 3. Allergen Inquiry (Safety-Critical)

**From**: Sarah Williams <swilliams.mom@gmail.com>
**Subject**: IMPORTANT - Gluten allergy question

**Email Body**:
```
My daughter has Celiac disease and we're trying to figure out if she can eat at Hattie B's.

Are your chicken tenders gluten-free? What about cross-contamination in the fryers?

We've been to places that say they're safe and she still gets sick, so I need to be really careful.

Sarah Williams
```

**Expected Routing**:
- **CinnaMon**: Neutral but high-stakes → normal flow
- **Hatch**: Retrieves allergen info if available
- **YGM**: Drafts response
- **QA**: Should FAIL or ESCALATE - safety-critical, requires human verification

**Expected Outcome**: REVISE or ESCALATE

**QA Checkpoints**:
- [ ] QA flags as high-risk (health/safety)
- [ ] Response doesn't make definitive safety claims
- [ ] Directs to manager/official allergen info
- [ ] Acknowledges severity of concern
- [ ] If KB has info, cites it but still recommends calling restaurant
- [ ] NO guessing about safety

---

## 4. Complaint - Wait Time (Negative Sentiment)

**From**: Mike Rodriguez <miker_1990@hotmail.com>
**Subject**: Extremely disappointed

**Email Body**:
```
I waited TWO HOURS for chicken yesterday at your Midtown location. TWO HOURS. I get that you're popular but this is ridiculous.

The food was good when I finally got it but I'm not sure I'll come back if I have to waste half my day standing in line. Do you do anything to manage the wait times or do you just not care?

Mike
```

**Expected Routing**:
- **CinnaMon**: NEGATIVE sentiment → priority escalation
- **Hatch**: May retrieve wait time info/policies
- **YGM**: Drafts empathetic response
- **QA**: Should PASS but flag for manager review (negative sentiment)

**Expected Outcome**: SHIP (with manager notification)

**QA Checkpoints**:
- [ ] Acknowledges frustration, no defensiveness
- [ ] Apologizes for experience
- [ ] Explains wait is due to cook-to-order quality
- [ ] Mentions call-ahead or off-peak options if available
- [ ] Offers something (discount/priority) if company policy allows
- [ ] Professional tone despite customer edge

---

## 5. Complaint - Wrong Order (Negative Sentiment)

**From**: Amanda Jackson <ajackson.design@gmail.com>
**Subject**: Got the wrong heat level - mouth is on fire

**Email Body**:
```
I ordered Damn Hot and got Shut the Cluck Up instead. I KNOW the difference. My mouth is on fire and I can't even finish the chicken I paid $15 for.

I called the restaurant and they said "sorry, mistakes happen." That's it. No offer to fix it, nothing.

Is this how you treat customers? I want a refund or at least an explanation of how this happened.

Amanda
```

**Expected Routing**:
- **CinnaMon**: NEGATIVE + specific complaint → escalation
- **Hatch**: May retrieve quality/refund policies
- **YGM**: Drafts service recovery response
- **QA**: Should FLAG for immediate manager review (complaint + refund request)

**Expected Outcome**: ESCALATE

**QA Checkpoints**:
- [ ] QA flags as complaint requiring compensation
- [ ] Response apologizes sincerely
- [ ] Acknowledges the mistake
- [ ] Offers to make it right (refund/replacement/credit)
- [ ] Explains quality standards
- [ ] Manager contact info provided
- [ ] No blaming staff or customer

---

## 6. Catering Inquiry (Handoff Required)

**From**: Robert Taylor <rtaylor@nashvilleevents.com>
**Subject**: Catering for corporate event - 150 people

**Email Body**:
```
Good morning,

I'm planning a corporate event for 150 people on March 15th and would love to have Hattie B's cater.

Can you handle an order this size? What's the process for catering? We'd need setup by 11:30am at our office in the Gulch.

Also need pricing and menu options - can we do a mix of heat levels?

Thanks,
Robert Taylor
Nashville Events & Co.
```

**Expected Routing**:
- **CinnaMon**: Neutral/positive, business inquiry → normal flow
- **Hatch**: May retrieve catering info if in KB
- **YGM**: Drafts response
- **QA**: Should FLAG for catering team handoff

**Expected Outcome**: ESCALATE (to catering department)

**QA Checkpoints**:
- [ ] QA identifies this needs specialist (catering team)
- [ ] Response is friendly and helpful
- [ ] Provides catering contact info or says "we'll have catering reach out"
- [ ] Confirms enthusiasm for the event
- [ ] Doesn't make commitments about pricing or availability
- [ ] Professional business tone

---

## 7. Positive Feedback (Positive Sentiment)

**From**: Emily Carter <emilycarter.food@gmail.com>
**Subject**: BEST CHICKEN OF MY LIFE

**Email Body**:
```
Oh my god. OH MY GOD.

I just had Hattie B's for the first time and I need you to know this is the best fried chicken I've ever eaten. I got the Hot level and it was PERFECT. The crunch, the spice, the juiciness - everything was incredible.

Your staff was so nice too! The guy at the register gave great recommendations and was patient with my million questions.

I'm from Seattle and am already planning my next trip to Nashville just to eat here again. Thank you for existing!!

Emily
```

**Expected Routing**:
- **CinnaMon**: POSITIVE sentiment → normal flow (may flag for social sharing)
- **Hatch**: No KB needed (pure feedback)
- **YGM**: Drafts grateful response
- **QA**: Should PASS easily

**Expected Outcome**: SHIP

**QA Checkpoints**:
- [ ] Warm, appreciative tone
- [ ] Thanks customer by name
- [ ] Acknowledges specific compliments (staff, heat level)
- [ ] Invites them back
- [ ] May mention social media or reviews
- [ ] Matches customer's enthusiasm without being over-the-top

---

## 8. Complex Multi-Question (Challenging)

**From**: Lisa Patel <lisapatel.travels@gmail.com>
**Subject**: Planning a visit - several questions

**Email Body**:
```
Hi!

My family is visiting Nashville in two weeks and we have some questions before we come:

1. We have a party of 8 including 2 kids (ages 6 and 9) - do you have a kids menu or mild options?
2. Can we make a reservation or is it first-come first-serve?
3. What sides do you recommend with the chicken?
4. Is there parking nearby or should we Uber?
5. My husband is vegetarian - do you have any non-chicken options?

Sorry for all the questions! We're really excited to try Hattie B's.

Thanks so much,
Lisa
```

**Expected Routing**:
- **CinnaMon**: Positive/neutral → normal flow
- **Hatch**: Needs to retrieve multiple KB sections (menu, kids options, parking, reservations)
- **YGM**: Drafts comprehensive response addressing all questions
- **QA**: Should PASS if all questions addressed accurately

**Expected Outcome**: SHIP (if KB has info) or REVISE (if missing key info)

**QA Checkpoints**:
- [ ] All 5 questions answered
- [ ] Answers in logical order
- [ ] Specific about kids options/heat levels
- [ ] Clear about reservation policy
- [ ] Honest about vegetarian options (limited)
- [ ] Helpful tone, not overwhelmed by multiple questions
- [ ] No made-up information

---

## 9. Out of Scope - Franchising (Edge Case)

**From**: James Wilson <jwilson.entrepreneur@gmail.com>
**Subject**: Franchise opportunity inquiry

**Email Body**:
```
To whom it may concern,

I'm a restaurant investor based in Atlanta and I'm very interested in bringing Hattie B's to the Georgia market.

Are you currently offering franchise opportunities? If so, who should I speak with about requirements and investment details?

Looking forward to hearing from you.

Best regards,
James Wilson
Wilson Restaurant Group
```

**Expected Routing**:
- **CinnaMon**: Neutral, business inquiry → normal flow
- **Hatch**: Unlikely to have franchising info in customer KB
- **YGM**: Drafts polite redirect
- **QA**: Should FLAG as outside customer service scope

**Expected Outcome**: ESCALATE (to corporate/business development)

**QA Checkpoints**:
- [ ] QA identifies as corporate/legal matter
- [ ] Response is professional and appreciative
- [ ] Doesn't say "yes" or "no" to franchising
- [ ] Provides corporate contact or says "we'll forward to appropriate team"
- [ ] No speculation about business plans
- [ ] Maintains brand positivity

---

## 10. Social Media Mention - Influencer (PR Sensitive)

**From**: Taylor Brooks <taylor@foodiefindsnashville.com>
**Subject**: Feature request for Instagram account (85K followers)

**Email Body**:
```
Hey Hattie B's team!

I'm Taylor, I run @FoodieFindsnashville on Instagram (85K followers). I'm putting together a "Nashville Hot Chicken Challenge" video series and would LOVE to feature Hattie B's as the ultimate destination.

Would you be open to:
- Letting me film in the restaurant during off-hours
- Possibly trying the Shut the Cluck Up on camera
- Interview with chef or owner about what makes Nashville hot chicken special

I always tag locations and this would be great exposure! My last Nashville restaurant feature got 200K views.

Let me know if you're interested!

Taylor Brooks
FoodieFindsNashville.com
```

**Expected Routing**:
- **CinnaMon**: Positive but business/PR inquiry → normal flow
- **Hatch**: Unlikely to have influencer/media policy in basic KB
- **YGM**: Drafts positive but non-committal response
- **QA**: Should FLAG for marketing/PR team review

**Expected Outcome**: ESCALATE (to marketing/PR)

**QA Checkpoints**:
- [ ] QA identifies as PR/marketing matter
- [ ] Response is enthusiastic and grateful
- [ ] Doesn't commit to filming or access
- [ ] Says "we'll connect you with our marketing team"
- [ ] Acknowledges follower count professionally
- [ ] Maintains brand voice (excited but not desperate)
- [ ] No promises about chef/owner availability

---

## Testing Protocol

### For Each Email:
1. **Input** the email into the system
2. **Monitor** each agent's output:
   - CinnaMon sentiment classification
   - Hatch context retrieval
   - YGM draft quality
   - QA evaluation and decision
3. **Verify** expected outcome matches actual
4. **Document** any failures or unexpected behavior

### Success Criteria:
- 90%+ correct sentiment detection (CinnaMon)
- 100% accuracy on factual KB information (Hatch)
- 80%+ responses need no revision (YGM + QA)
- 100% of safety-critical emails flagged (QA)
- 0% hallucinated information ships to customers

### Common Failure Modes to Watch:
- **Over-confidence**: QA passes responses that need human review
- **Under-confidence**: QA fails good responses unnecessarily
- **Hallucination**: YGM invents menu items, policies, or promises
- **Tone mismatch**: Wrong energy level for customer sentiment
- **Incomplete answers**: Missing questions in multi-part emails
- **False escalation**: Simple questions routed to managers

---

## Notes for Students

**These emails are based on real customer service patterns**:
- Heat level questions are the #1 inquiry
- Wait time complaints are common for popular restaurants
- Allergen questions require extreme caution
- Multi-question emails test information synthesis
- Edge cases (franchising, PR) test proper escalation

**When building your own agent system**, create similar test suites covering:
- Happy path (easy wins)
- Edge cases (unusual requests)
- Safety-critical scenarios (where failure has consequences)
- Negative sentiment (service recovery)
- Out of scope (proper handoffs)

**The goal isn't perfection** - it's knowing what your system can handle autonomously vs. when it needs human judgment.
