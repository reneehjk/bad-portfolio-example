#!/usr/bin/env python3
from pathlib import Path

paras = r'''
This project was a fintech app for everyday money management. The product helps people see their balance, send payments, and keep track of spending in one place. I joined as the product designer on a small team with a product manager, two engineers, and a researcher. The timeline was roughly four months. The company wanted a more user-centric experience that would feel seamless and intuitive for people who use the app in short sessions on their phones, often while doing something else.

My role covered the end-to-end design of the core flows: onboarding, home, payments, activity, and account. I ran research sessions with the researcher, synthesized findings, proposed a direction, designed wireframes and high-fidelity screens, prototyped the main paths, and supported testing. I also maintained a small component set in Figma so the screens would stay consistent. Day to day I sat in standups, brought work to critiques, and partnered with engineering on what we could realistically ship in the window we had.

The existing product already worked in the sense that people could create an account and move money. What it did not do well was feel clear. New users were dropping off during sign-up. Returning users were sending the same support questions about whether a payment had gone through. The business wanted more people to finish onboarding and more people to complete a first transfer in the first week. Those were the goals I was asked to design toward, and they shaped the work even when the conversation in the room was about visual polish.

We framed the problem as a gap between what the product could do and what it felt like to do it. Users wanted a better, more intuitive experience. They needed to trust that their money was where they thought it was. They needed to finish set-up without feeling like they were filling out paperwork. They needed a home screen that answered “am I okay?” in a glance. That is a real problem, and it is also a very common one in this category. Our job was to bridge the gap between those user needs and the business need to activate and retain people.

The primary person we designed for is Sarah, 28, a busy professional. Sarah uses her phone for almost everything. She does not want to learn a financial product. She wants to send rent, check that her paycheck landed, and move on with her day. She is comfortable with technology but impatient with extra steps. She will abandon a flow if it asks for the same information twice. She is the kind of user who keeps four banking apps and still is not sure which one is “the main one.” Designing for Sarah meant optimizing for speed, reassurance, and plain language.

I want to be thorough about how we got to that picture of Sarah, because the persona was not invented in a vacuum. We conducted user interviews. We sent out a survey. We listened to support call snippets. We looked at funnel data for sign-up and first payment. Interview participants described similar moments: opening the app on a bus, not being sure if a transfer was pending or failed, closing it, checking email, opening it again. Survey responses pointed at the same themes in more compressed language — confusing, slow, not sure if it worked. We wrote those themes on a board and lived with them for the rest of the project.

The interviews were semi-structured. We asked people to walk us through the last time they sent money to a person or a bill. We asked them to show us the apps they already use. We asked what “done” feels like. We did not ask them to redesign our product. We asked them to narrate their own. That distinction matters because people are better at telling you what they did than at specifying a UI. We took notes, recorded with permission, and later pulled quotes into an affinity map. The map is where “I just want to know it went through” clustered into a blob we kept pointing at.

Survey questions covered frequency of use, devices, and ratings of current confidence during a transfer. We also asked an open field about the last time something felt unclear. The qualitative comments were more useful than the scores. Scores told us people were lukewarm. Comments told us they could not tell pending from complete, and that onboarding felt like a credit application. Those two sentences did more for the project than any chart, though we still made the chart because stakeholders like charts.

I also sat with the current app myself and wrote a step-by-step of onboarding and a first payment. There were nine screens before a person could see a home balance, including two that asked for overlapping personal details. The payment flow had a review step that looked almost identical to the amount step, then a success screen that used the word “submitted” instead of “sent.” Small language choices were creating large doubts. Documenting the current path was unglamorous and necessary. It gave us a shared artifact so we were not arguing from memory.

Competitive review was part of the research, carefully. We looked at other fintech apps and traditional banking apps, not to copy a pattern for its own sake but to understand what Sarah already knows how to do. Confirmation patterns, PIN versus biometric, how balances are shown, how pending transactions are labeled — these are learned behaviors. If we invented a new way to confirm a payment, we would be asking people to unlearn something. We noted where competitors were clear and where they were noisy. We brought three screenshots to a working session and talked about them like a study group.

Synthesis took longer than the sessions. It always does. We grouped notes into needs: feel safe, finish fast, understand status, recover from mistakes. We wrote a problem statement that we revised three times. The version we used was: busy people cannot tell if their money moved, and they stall during set-up because the product asks them to prove who they are before it has proven it is useful. That sentence is long. We kept it long so we would not flatten the problem into “make it nicer.” Making it nicer was not the assignment. Making status obvious and set-up tolerable was the assignment.

I want to pause and restate that, because it is easy to lose in a write-up this detailed. The problem was not visual fashion. The problem was that onboarding felt like paperwork and payments did not close the loop. If we had only redesigned colors and type, we would have failed even if the screens looked more delightful. Delight in this context is the relief of knowing a transfer worked. That is the kind of delight that is actually user-centric rather than decorative.

We turned the problem into how-might-we prompts. How might we show Sarah her money is okay within two seconds of opening the app. How might we get her to a useful home before we collect every document. How might we make payment status impossible to misread. How might we let her recover when she types the wrong amount. These prompts hung in FigJam and we came back to them whenever a screen started to accumulate extras. Extras are how products get unclear again.

Ideation was structured. We sketched separately for twenty minutes, then explained the sketches, then dotted the ones that best answered the prompts. I am describing this in detail because the method is the work as much as the output. We did not jump to Figma. We stayed lo-fi until we had a sequence: a shorter onboarding, a home that leads with balance and recent activity, a payment flow with one review, a status that uses everyday words. The winning sketch for payments was almost boring. Boring was the point.

Onboarding was the hardest negotiation. Compliance needs identity information. Users need to see value. We proposed a split: create an account with email and a passcode, land on home with a limited balance view, then complete verification when the person tries to send more than a small amount or add a bank. Legal was uncomfortable. Engineering was comfortable. We met in the middle: collect the minimum legally required up front, defer the rest, and write the deferred steps as “unlock sending” rather than “please finish your profile.” The language change mattered. Profile completion sounds like homework. Unlocking sending sounds like a benefit.

I will walk through that onboarding decision again from the user’s side, because it is easy to describe as a process and forget the feeling. Sarah downloads the app because a friend mentioned it. She is not in a paperwork mood. If we greet her with a long form, she leaves. If we greet her with a home screen that already looks like her money, she stays long enough to trust us with the rest. That is why we fought for a useful first screen even when it made the data model messier. The mess is on our side. The clarity is on hers.

Home design started with a hierarchy argument. I wanted balance first, then upcoming bills, then recent activity. The PM wanted a product card for a new savings feature. We tested both. People looked at the savings card, did not tap it, and still asked where their balance was. We shipped balance first. The savings feature got a smaller entry lower on the page. That is a trade-off. The business still got a surface. Sarah still got an answer. I mention the alternative because the choice was not inevitable; it was a decision after we watched people miss the number.

Payments needed a sequence that matched how people talk. Who, how much, confirm, done. The old flow mixed those together and asked for a memo in the middle. We moved memo to optional on the confirm step. We made the confirm screen look different from the amount screen so it would feel like a checkpoint. We replaced “submitted” with “sent” when the transfer was instant, and “pending — usually arrives by Tuesday” when it was not. Specificity is kindness in fintech. Vague success is how support queues grow.

There was an alternative payment design I liked and did not ship. It was a single long screen with everything on it, Apple-Pay style. It photographed well. In testing, people missed the recipient field because they jumped to the number pad. We went back to a short sequence of screens. I still think the long screen could work with better focus management. We did not have time to get it there, and a missed recipient is an unacceptable risk. That is the kind of trade-off that does not show up if you only look at the final mockups.

Activity — the list of transactions — sounds simple and was not. People use it as a receipt drawer. They search for a name. They need pending items to look different from settled ones without looking alarming. We used a quiet label and a different secondary color, not a red warning, because pending is normal. We added a simple filter for “from me” and “to me” after two interview participants scrolled hunting for a paycheck. Search was scoped to names and amounts only. Full-text search across memos was an engineering stretch we cut.

Account and settings were cleaned up rather than reinvented. We grouped security, connected banks, and notifications. We did not hide the log-out button. We wrote the empty state for no connected bank as an instruction with a button, not a cheerful illustration with no next step. These are small pages and they are where trust quietly lives. I am including them in this write-up because case studies that only show the hero flow pretend the product is three screens.

Visual design stayed calm on purpose. A fintech app that looks like a lifestyle brand can feel unsafe. We used a restrained palette, clear type hierarchy, and plenty of space around numbers. We made amounts the loudest element on payment and home. We did not use illustration on the success state; we used a check and a sentence. I am not claiming this is original. I am claiming it is appropriate. User-centric in this category often looks like restraint.

We built a prototype that covered sign-up through first payment and a second path for a returning user checking a pending transfer. Prototyping the returning path was as important as the first-run. Most of the life of the product is the returning path. If you only prototype onboarding, you polish the front door and leave the house unfinished. The prototype used real-looking amounts and names because lorem ipsum makes people polite in tests. Polite tests are useless.

Testing included six usability sessions on the new flows and a comparison pass against the old onboarding with three people who had never seen either. I am describing the method because “we tested” is not information. We gave them a task: get set up and send $40 to a person named Priya. We watched where they hesitated. We asked them to think aloud. We did not help unless they were fully stuck. Afterward we asked them to rate how sure they were that the money moved. Certainty was the metric we cared about, not smiles.

Findings from testing were specific. People still stumbled on a permissions screen that looked like a legal wall. We rewrote it to one paragraph and a continue button, with details behind “learn more.” Two people tried to tap the balance on home expecting a breakdown; we made that tap open activity filtered to this month. One person did not see the pending label. We increased contrast and moved it next to the amount instead of under the merchant name. These are not glamorous changes. They are the reason the final version is more intuitive than the middle version.

I want to talk about what we did not change, because constraints are part of the design. We could not remove identity verification. We could not show certain balances until a bank was linked. We could not offer instant transfer on every rail. The design had to tell the truth about speed. If we had labeled everything “instant” it would have been delightful for a day and damaging after the first ACH. Honesty is a product decision. It showed up in copy more than in layout, which is why copy sat in the Figma file next to the components, not in a side document nobody opened.

Collaboration with engineering started in wireframes, not at handoff. We flagged the deferred verification state early so they could model it. We cut an animation on the success screen when it threatened a sprint. We kept the component names aligned with their repo so a button was a button. None of this is exciting to read and all of it is how a design actually ships. A seamless experience for users is often a slightly inelegant compromise in the codebase. I would rather ship the compromise than keep a perfect file.

I should also mention the research-to-design link in one more way, because it is the spine of the project. Interviews said status was unclear, so we redesigned status language and placement. Funnels said onboarding dropped at personal details, so we deferred details. Sarah’s short sessions said home must answer one question fast, so we put the number at the top even when marketing wanted a campaign module there. If a screen in the file cannot be traced to one of those inputs, it probably did not need to exist. We killed a few of those.

There was a mid-project moment where the work could have become a visual refresh. A stakeholder liked a more colorful exploration. It was a valid aesthetic. It did not help someone know whether rent had landed. We showed the two homes side by side with the task “find out if you can pay rent today.” People were faster on the quieter one. That test is why the final UI is quieter. I am repeating the theme on purpose: we kept choosing clarity over novelty. In a portfolio it can look conservative. In a fintech app it is the assignment.

Documentation for handoff included flows, states, empty and error, and a short writing guide for status. Error messages were written as what happened and what to do next. “We couldn’t send this. Check the amount and try again” is not poetry. It is usable. We listed edge cases: no network, insufficient funds, recipient not found, verification needed. Engineers added two I had missed. The file got a cover with how to navigate it. Handoff is design. Leaving a puzzle is not.

After launch we watched the same funnels we had at the start. More people finished onboarding. More people completed a first transfer in the first week. Support tickets about “did this go through” went down. I am not going to pretend a single redesign is the only cause — messaging and a small promotion ran in the same month — but the qualitative notes from support shifted from confusion to ordinary account questions. That shift is what I was hoping for. The product did not become a different product. It became a clearer version of itself.

If I am honest about impact, the work succeeded where we had been specific — status, onboarding length, home hierarchy — and it did less for a vague hope that people would “engage more” with extra features. They did not. They paid people and checked balances. That is the job. I would rather design a seamless experience of the job than a delightful layer on top of a confusing one. Bridging the gap between users and business, in this case, meant helping the business win by helping Sarah finish something she already came to do.

Looking back, I would have pulled a writer in earlier. A lot of the improvement was language, and I am a designer who writes, not a writer. I would have tested with a couple of people who are less comfortable with apps; our panel skewed confident. I would have scoped activity search more ambitiously if we had another sprint. Those are real gaps. They do not undo the core decisions. They are the next ones.

I have described this at length because the project was not a single insight and a hero shot. It was a series of ordinary decisions that added up: split onboarding, lead with balance, make confirm look like confirm, say pending when it is pending, defer the savings pitch, write errors like a person. Each one is small. Together they are the difference between a fintech app people abandon and a fintech app people finish. That is the story. It takes a while to tell if you tell it honestly.

The team dynamic is worth a few more words because product design does not happen in a vacuum. The PM protected time for research when there was pressure to start pixels. The researcher kept us from treating three loud interview moments as a trend. Engineering told us no with reasons, which is a gift. I brought options instead of a single file when a decision was actually a decision. The work is more user-centric when the team is allowed to be specific. I try to be the person in the room who keeps pointing at the task Sarah is trying to finish.

On a typical week I would look at a flow in the morning, take it to critique, revise in the afternoon, and ping engineering about a state we had forgotten. Evenings before tests were spent making the prototype feel less like a deck and more like a phone. After tests I wrote notes the same day, because notes from memory are fiction. This rhythm is not unique. I am including it so the process is not a mysterious cloud of “design thinking.” It is a calendar. It is a series of artifacts. It is conversations that change the file.

Sarah appears throughout this story because she was useful. She is a template of a real pattern: busy, competent, unwilling to study the app. Whenever we added a step we asked whether she would do it on a sidewalk. Whenever we added a modal we asked whether she would understand it at a glance. Personas can become theater. We tried to use hers as a constraint, the way a smaller viewport is a constraint. If it did not fit Sarah’s two-minute session, it waited.

I realize I have now explained onboarding more than once. I am leaving the repetition in, because that is where the project lived. We talked about onboarding in week one and week eight. We talked about it after legal review and after the first test. We talked about it when a new stakeholder joined and wanted a tutorial carousel. We did not add the carousel. Tutorials are what you ship when the UI cannot explain itself. Our bet was that a useful home explains itself better than a tour of a locked home. I still think that is right.

Payments, too, I have described from several angles, and they deserve it. Money movement is the product. Everything else is support. The final payment flow is who, amount, confirm, done, with status that can be read in the list later. It is not clever. It is aligned with how people already send money elsewhere. Aligning with existing mental models is how you get an intuitive experience without making anyone learn your brand of intuition. Invented gestures are not user-centric. They are designer-centric.

There is a version of this case study that is three paragraphs and a row of phones. I did not write that version, because I wanted a hiring manager to see the reasoning, the constraints, the alternatives, and the outcome in one place. The phones are in the file. The reasoning is here. If you have stayed with this write-up, you now know what I would argue for in a critique: fewer steps before value, numbers that speak first, language that tells the truth about time, and no extra modules above the thing the person opened the app to see.

The outcome, stated plainly, is this. We shipped a clearer fintech app. Onboarding completion improved. First transfers improved. “Did it go through” tickets declined. Sarah, or people like her, can see a balance quickly and send money without wondering what “submitted” means. The business got closer to the activation numbers it wanted. The design system is small enough to maintain. The remaining issues are listed. That is a complete piece of product design work. It just takes a long time to walk through every step without skipping the parts that were actually the job.

I keep coming back to the phrase solving real problems because it is easy to say and harder to stay with. The real problem was not that the app lacked delight in the abstract. The real problem was a person on a bus who could not tell if rent was paid. Every decision I have written down here is in service of that person. If a future project does not have a sentence that clear, I would want to keep researching until it does. Clarity about the problem is what makes the screens make sense. Without it, you just have screens.

This write-up is long because the work was a chain, and I did not want to cut the chain into a highlight reel. You have the context, the role, the problem, the research, the decisions with their alternatives, and the outcome. You also have the weekly texture of how those things happened. That is what I can offer from this fintech project: not a magic trick, a record of choosing the more obvious path on purpose, again and again, until the experience felt seamless for someone who was never going to give us more than a minute.
'''

paragraphs = [p.strip() for p in paras.strip().split("\n\n") if p.strip()]

body = "\n".join(f"      <p>\n        {p}\n      </p>" for p in paragraphs)

html = f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>A Fintech App — Alex Morgan</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="css/styles.css" />
    <link rel="stylesheet" href="css/case.css" />
  </head>
  <body class="page-case text-heavy">
    <header class="site-header">
      <a class="brand" href="index.html">
        <span class="brand-name">Alex Morgan</span>
        <span class="brand-title">Product Designer</span>
      </a>
      <nav class="site-nav">
        <a href="index.html">Work</a>
        <a href="about.html">About</a>
        <a href="contact.html">Contact</a>
      </nav>
    </header>

    <div class="wrap">
      <p class="muted" style="margin: 0 0 8px; font-size: 12px;">Product design · 2024</p>
      <h1>A Fintech App</h1>
      <p class="lede">
        Designing a more user-centric money experience — from the first session through
        a completed payment — for people who do not have time to learn a new product.
      </p>
      <div class="shot" style="margin-bottom: 32px;">
        <img src="assets/skb-hero.svg" alt="Fintech app screens" />
        <p class="caption">[Image: final mobile screens for home, payments, activity, and account]</p>
      </div>
{body}
      <p>
        [Image: onboarding and first-payment prototype, available in the working file]
      </p>
    </div>

    <footer class="site-footer">
      <span>© 2026 Alex Morgan</span>
      <span>Open to new opportunities</span>
    </footer>
  </body>
</html>
'''

out = Path(__file__).resolve().parents[1] / "fintech-app.html"
out.write_text(html, encoding="utf-8")
words = len(__import__("re").findall(r"[A-Za-z0-9']+", paras))
print("paragraphs", len(paragraphs), "words", words, "min", round(words / 225, 1))
