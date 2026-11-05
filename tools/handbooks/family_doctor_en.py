# Content: Tadawa Family Doctor Workflow Handbook (revised 2026-10-28)
# Source: Google Doc 1gL0Sf-oD-s5tcCnWZLf8CpbWz76QAUQoveGJ6T7IXkk, open suggestions applied.

def tel(num, label=None):
    digits = "".join(ch for ch in num if ch.isdigit() or ch == "+")
    return f'<a class="approval-number" href="tel:{digits}">{label or num}</a>'

def ext(href, text):
    return f'<a href="{href}" target="_blank" rel="noopener noreferrer">{text}</a>'

TAF = "<strong>#Tafileh Clinic 24/7</strong>"
CREDS = "https://docs.google.com/document/d/1KGv76GOxYmgfNo-96zjzKN2I6B_k04fhl7U8lVrHW24/edit"
PROTOCOL = "https://docs.google.com/document/d/1AvCENNEc172oMpsQ3PbRUv6emGKrrjTFv85Nit3CV2o/edit"
REPORT_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSebHeUZV1w2hwW8F9vvzqLqnmDQAPwpniKvQZVJ4YIpBUW7QQ/viewform"
TM_HANDBOOK = "https://docs.google.com/document/d/1vfk7wv086Ctd1u6TRq80M52nNTWU3hg4DwADnC7UqKc/edit"

META = dict(
    lang="en",
    one="section",
    many="sections",
    title_tag="Family Doctor Workflow Handbook – Tadawa",
    eyebrow="Tadawa Healthcare · Family Medicine",
    h1="Family Doctor Workflow Handbook",
    lede="For Family Doctors working remotely or at Tadawa clinics, alongside the Tafileh team.",
    tags=["15 sections", "Revised 28 October 2026", "Version 1 · October 2026"],
    home_aria="Tadawa handbook home",
    progress="Reading progress",
    toc_aria="Handbook contents",
    search_heading="Find a section",
    search_label="Search the handbook sections",
    search_ph="Search for a rule or task…",
    empty="No section matches. Try a shorter word.",
    intro_h="Use the handbook by task",
    intro_p="Daily reference for Tadawa Family Doctors. Search shows the sections that contain your word and opens any folded steps that match.",
    quick_aria="Key reminders",
    footer_h="Tadawa · Family Doctor Workflow Handbook",
    footer_p="Revised 28 October 2026. Check rules and contacts against current internal instructions.",
    note=f"""
      <div class="credential-note" role="note">
        <b>Restricted</b>
        <span>Insurance portal logins and step-by-step portal entry are not in this handbook. They are in a separate restricted document: {ext(CREDS, "Insurance Portals &amp; Credentials – Family Doctors Only")}.</span>
      </div>
""",
)

QUICK = [
    ("Log out completely off shift", "\"Away\" or \"Not available\" is not enough. An open Tadawa tab, even on your phone, can route Treat Me Now calls to you."),
    ("Save every consultation", "If you do not click \"Save consultation\" you stay Busy and will not receive new calls."),
    ("ER referral: two different labels", "On MedNet select \"general\". On Tadawa select \"ER / Emergency Medicine\"."),
]

CHAPTERS = [
dict(id="role", toc="Your role", kicker="Foundation", group="teal", title="Your role", body=f"""
        <p>Tadawa has Family Medicine specialists only on the platform. You handle Treat Me Now calls, remote appointments, care plan requests and in-clinic consultations with the Tafileh team.</p>
        <div class="callout">
          <strong>You are the gatekeeper</strong>
          <p>You decide whether a referral to a specialist or the ER is needed, and you make the referral on the insurer portal.</p>
        </div>
        <div class="info-grid">
          <section class="info-card">
            <h3>On-site General Practitioners</h3>
            <p>Triage patients in Tafileh and act as your assistant doctors. They do not open insurance forms or order labs, imaging or medication.</p>
          </section>
          <section class="info-card">
            <h3>Family Doctors only</h3>
            <p>Open forms on insurer portals (including GP-type accounts), order tests and prescribe.</p>
          </section>
        </div>
        <p>You also work with the nurses and secretaries in Tafileh. When we refer a patient to a specialty, the insurer opens access to all in-network specialists of that type and the patient chooses the doctor.</p>
"""),

dict(id="shifts", toc="Shifts and communication", kicker="Team", group="teal", title="Shifts and communication", body=f"""
        <ul>
          <li><strong>Check in:</strong> at the start of every shift, post a check-in in the {TAF} group with the shift (A/B/C) and who is on with you (GP, nurse, Family Doctor).</li>
          <li><strong>Swaps and absences:</strong> announce any swap, absence or change in hours in the {TAF} group and tag the secretary so your hours on the system are updated. Appointments are booked according to the doctor shown on the schedule.</li>
          <li><strong>Shift C (on-call):</strong> at the end of Shift B the clinic phone line is forwarded to the on-call Family Doctor, and staff post a confirmation in the {TAF} group.</li>
          <li>Doctors working from outside Jordan are contacted on Zoho Cliq, not by phone.</li>
          <li>All-staff meetings are announced in <strong>#announcements</strong> and attendance is mandatory.</li>
        </ul>
        <div class="callout success">
          <strong>Doctors' morning report</strong>
          <p>Daily at about 8:45 AM on Zoho Meeting, inside Zoho Cliq. Secretaries do not attend.</p>
        </div>
        <h3>Zoho Cliq channels</h3>
        <div class="reference-list">
          <div class="reference-row"><strong>#announcements</strong><span>Official circulars – check regularly.</span></div>
          <div class="reference-row"><strong>#Tafileh Clinic 24/7</strong><span>Daily operations.</span></div>
          <div class="reference-row"><strong>#Medical discussions</strong><span>Clinical discussions – all doctors should join; secretaries and nurses do not join.</span></div>
          <div class="reference-row"><strong>#IT-Support</strong><span>Tadawa platform problems.</span></div>
          <div class="reference-row"><strong>#Chronic Reports</strong><span>You post the chronic medication report text; the secretary posts back the stamped, scanned report.</span></div>
        </div>
        <div class="callout warning">
          <strong>Patient data</strong>
          <p>Share patient data only in the authorised channels. Never post login screenshots or passwords in any group. Use private messages for one-to-one follow-ups.</p>
        </div>
"""),

dict(id="routing", toc="Status and call routing", kicker="Calls", group="violet", title="Status and call routing", body=f"""
        <div class="callout warning">
          <strong>Off shift means logged out</strong>
          <p>When off shift, log out completely. "Away" or "Not available" is not enough. Opening Tadawa while off shift, even on your phone to check a patient file, can route Treat Me Now calls to you; log out immediately afterwards.</p>
        </div>
        <ul>
          <li>The secretary may contact you on phone while you are off shift to follow up on a patient you saw.</li>
          <li>Keep Tadawa open in only one browser tab.</li>
          <li><strong>Patients cannot choose a doctor;</strong> the system routes the call to an available doctor. If a patient asks for a specific doctor, the other doctors set themselves to "Not available" until the call connects, then switch back to "Available".</li>
          <li><strong>The status at the top of the screen is the one that counts.</strong> If it conflicts with your profile, or callers get "busy" while you are Available, switch to Unavailable and back to Available.</li>
          <li>If the doctor who receives a call does not answer, the call is not passed on. The patient has to call again, and the next attempt goes to an available doctor.</li>
          <li>If a call rings while you are marked Not available or Away, report it with a screenshot in <strong>#IT-Support</strong>.</li>
        </ul>
        <details class="workflow" open>
          <summary>Callback Queue</summary>
          <div class="workflow-content">
            <ol>
              <li>If all Family Doctors are busy, the patient is told no doctor is available.</li>
              <li>All eligible Family Doctors and the clinic secretary get a missed-call notification, and a consultation with the status "Missed Call" appears in the appointments table and on the dashboard.</li>
              <li>Click "Call Back Patient" to call the patient (it can take about a minute to open).</li>
              <li>If the call-back does not connect, ask the clinic to call the patient by phone.</li>
            </ol>
          </div>
        </details>
        <div class="callout success">
          <strong>Call priority</strong>
          <p>Emergencies always come first. If you are busy and another patient's call is missed, the secretary calls that patient to say you will call back as soon as you finish.</p>
        </div>
"""),

dict(id="consultation", toc="Running a telemedicine consultation", kicker="Clinical", group="green", title="Running a telemedicine consultation", body=f"""
        <p>Summary of the {ext(TM_HANDBOOK, "Tadawa Telemedicine Doctor Handbook")}. Read the full handbook once; use this section as a quick reference.</p>
        <p class="sub-label">The Tadawa Golden Rule</p>
        <ol class="golden-rule">
          <li>Ask</li><li>Observe</li><li>Assess</li><li>Decide</li><li>Explain</li><li>Safety-net</li><li>Document</li>
        </ol>

        <details class="workflow">
          <summary>Before the call</summary>
          <div class="workflow-content">
            <ul>
              <li>Review the record: previous consultations, diagnoses, medications, allergies and results.</li>
              <li>Check your camera, microphone and internet.</li>
              <li><strong>Professional presence:</strong> professional dress (working from home does not change this), a plain or office background, front lighting, camera at eye level, a quiet private room, no food, no personal calls and nobody else in view.</li>
            </ul>
          </div>
        </details>
        <details class="workflow">
          <summary>Opening</summary>
          <div class="workflow-content">
            <div class="template-box">"Hello, I'm Dr. ___, one of the family physicians at Tadawa. Can you hear and see me clearly?"</div>
            <ul>
              <li>Confirm full name, date of birth and identity. For children, confirm the guardian's name and relationship.</li>
              <li>Ask where the patient is (essential if they may be unstable: exact location, who is with them, access to emergency services).</li>
              <li>Confirm privacy and who else is present. Start with an open question: "How can I help you today?"</li>
            </ul>
          </div>
        </details>
        <details class="workflow">
          <summary>History, vitals and examination</summary>
          <div class="workflow-content">
            <ul>
              <li>Take a structured history: presenting complaint, relevant history, all medications and supplements, allergies (drug, reaction, severity).</li>
              <li>Actively screen for red flags (chest pain, headache, abdominal pain, breathing). <strong>Red flags trigger a decision, not more questions.</strong></li>
              <li>Ask for available measurements (temperature, BP, heart rate, SpO₂, glucose, weight) and when they were taken. Ask to see the device on camera if important.</li>
              <li>Remote examination is limited. Do not use self-palpation to rule out an acute abdomen. Do not document a normal ear drum unless it was actually seen. Do not make a confident diagnosis from poor images.</li>
              <li><strong>Children:</strong> confirm weight; observe alertness, feeding, breathing and hydration. Give guardians simple instructions; never ask them to "perform an examination".</li>
            </ul>
          </div>
        </details>
        <details class="workflow">
          <summary>Decide</summary>
          <div class="workflow-content">
            <p><strong>Can I safely manage this patient remotely?</strong></p>
            <div class="info-grid">
              <section class="info-card"><h3>Yes</h3><p>Continue.</p></section>
              <section class="info-card"><h3>Maybe / uncertain</h3><p>Arrange an in-person assessment.</p></section>
              <section class="info-card"><h3>No / possible emergency</h3><p>Urgent or emergency referral.</p></section>
            </div>
            <p>Before prescribing, check diagnosis, allergies, current medications, interactions, contraindications, pregnancy, renal/hepatic issues, dose, frequency, duration and follow-up. Do not prescribe only because the patient asks.</p>
          </div>
        </details>
        <details class="workflow">
          <summary>Close</summary>
          <div class="workflow-content">
            <ul>
              <li>Explain the likely diagnosis, the treatment, what to expect and what to do if there is no improvement.</li>
              <li><strong>Safety-netting is mandatory</strong> and specific to the problem.</li>
              <li>Never end with "follow up as needed" alone when follow-up matters: say when, where and who is responsible.</li>
              <li>Confirm understanding (ask the patient to repeat how they will take the medication and which symptoms need urgent care).</li>
            </ul>
          </div>
        </details>
        <details class="workflow">
          <summary>Document</summary>
          <div class="workflow-content">
            <ul>
              <li>Date/time, modality, identity, participants, location if relevant, consent.</li>
              <li>Complaint, history, medications, allergies, vitals, remote examination, assessment and plan (treatment, investigations, referral, follow-up, safety-netting).</li>
              <li>Write <em>"Physical examination was limited by the telemedicine format"</em>, then document what you actually observed.</li>
            </ul>
          </div>
        </details>

        <h3>Emergency suspected</h3>
        <div class="callout warning">
          <strong>Stop the routine consultation</strong>
          <p>"I am concerned about your symptoms and I don't think it is safe to manage this through telemedicine alone."</p>
        </div>
        <ol>
          <li>Establish the patient's location and who is with them, and assess immediate safety.</li>
          <li>Direct the patient to emergency care, make the referral (<a href="#referrals">Section 10</a>) and report in the {TAF} group.</li>
          <li>Document the recommendation, whether the patient accepted, and any contact with the receiving facility.</li>
        </ol>
        <div class="callout warning">
          <strong>Never</strong>
          <p>Pretend an examination was done; give false reassurance; continue video with an unstable patient; delay an emergency referral; prescribe antibiotics just because they are requested; end without a safety net.</p>
        </div>
"""),

dict(id="troubleshooting", toc="Treat Me Now troubleshooting", kicker="Calls", group="violet", title="Treat Me Now troubleshooting", body=f"""
        <div class="info-grid">
          <section class="info-card">
            <h3>Patient does not join</h3>
            <p>Ask the secretary or nurse in the {TAF} group to call the patient. The patient can rejoin the same call with the reconnect button. Wait up to 10 minutes. If the patient still has not joined, cancel the consultation so the patient is not charged.</p>
          </section>
          <section class="info-card">
            <h3>Patient drops during the call</h3>
            <p>Wait 5 minutes for the patient to call back, then save the consultation.</p>
          </section>
        </div>
        <details class="workflow" open>
          <summary>No sound</summary>
          <div class="workflow-content">
            <ul>
              <li><strong>Patient side:</strong> update the Tadawa app, allow the microphone, turn off Bluetooth and use speakerphone.</li>
              <li><strong>Your side:</strong> allow the microphone and camera in the browser, test at {ext("https://mictests.com/", "mictests.com")}, close other apps and Tadawa tabs, then refresh or restart.</li>
              <li><strong>Still no sound:</strong> continue on Zoho Cliq, or by phone through the clinic, or let the secretary connect you with the patient.</li>
            </ul>
          </div>
        </details>
        <div class="callout open-point">
          <strong>After every call</strong>
          <p>Click "Save consultation". If you do not save, you stay "Busy" and will not receive new calls. If your status looks wrong or calls do not arrive: switch to Unavailable and back to Available, refresh, and keep Tadawa in one tab only.</p>
        </div>
        <div class="callout warning">
          <strong>Tadawa is down</strong>
          <p>See patients on Zoho Cliq and record the visits on Tadawa once it is back. Report it in #IT-Support with a screenshot.</p>
        </div>
"""),

dict(id="appointments", toc="Appointments, care plans and orders", kicker="Schedule", group="violet", title="Appointments, care plans and orders", body=f"""
        <ul>
          <li>Today's appointments are on the dashboard; later ones are in the Appointments section. Search a patient's name in Appointments to see previous visits.</li>
          <li><strong>Telemedicine appointments:</strong> click "Start consultation" at the appointment time. The patient cannot join early. The appointment stays open about 2 hours, but the system waits only about 15 minutes for the patient.</li>
          <li><strong>Care plan requests:</strong> open the request. If the patient gave enough information, create the care plan. If not, the secretary books a remote appointment with you.</li>
          <li>Appointments made by the Irbid clinic may appear on our dashboard; check with the Irbid group before cancelling.</li>
        </ul>
        <div class="callout">
          <strong>Orders</strong>
          <p>Always add lab and imaging orders in the orders section on Tadawa; otherwise the patient cannot see them. Patients can upload results in the app or send them to the clinic WhatsApp.</p>
        </div>
"""),

dict(id="documentation", toc="Documentation rules on Tadawa", kicker="Records", group="green", title="Documentation rules on Tadawa", body=f"""
        <div class="info-grid">
          <section class="info-card"><h3>Public notes</h3><p>Visible to the patient and all treating doctors.</p></section>
          <section class="info-card"><h3>Private notes</h3><p>Seen only by the doctor who wrote them.</p></section>
        </div>
        <ul>
          <li>The patient should call from their own (sub-account) profile so the claim and notes are recorded under the right person.</li>
          <li><strong>A parent calls from their own account for a child:</strong> document the consultation under the child, remove diagnoses and medications from the parent's record, and keep the parent's note with a disclaimer that the call was for the child.</li>
          <li><strong>Drug not in Tadawa's medication list:</strong> write it in the note and prescribe it on the insurer portal. Send missing drug names to the IT team in #IT-Support. Report wrong dosage forms (e.g., tablet listed as liquid) through the reporting form (<a href="#reporting">Section 13</a>).</li>
        </ul>
"""),

dict(id="medications", toc="Medications, sick leaves and reports", kicker="Prescribing", group="green", title="Medications, sick leaves and reports", body=f"""
        <h3>Chronic medications</h3>
        <p>A formal medical report is required for chronic medications, including dose changes or a new chronic medication. The patient submits it to the insurer for coverage approval.</p>
        <ul>
          <li><strong>Before writing it:</strong> confirm the patient is taking the medication, check the date of the last follow-up labs, and order labs if needed.</li>
        </ul>
        <p class="sub-label">Wording</p>
        <div class="template-box">"Patient [name, age, date] was seen at our Tafileh centre and suffers from [condition]. He/she requires [drug, dose] as a chronic medication."<br>Sign with your name and "Family Medicine Specialist".</div>
        <p>The template (<span lang="ar" dir="rtl">تقرير طبي للأدوية المزمنة</span>) is available from the secretariat.</p>
        <details class="workflow" open>
          <summary>From your text to the patient's PDF</summary>
          <div class="workflow-content">
            <ol>
              <li>Send the report text to the secretary on Zoho Cliq in the <strong>#Chronic Reports</strong> channel.</li>
              <li>The secretary puts it on the Tadawa Healthcare letterhead, prints, stamps and scans it.</li>
              <li>The secretary sends the scanned copy to the patient through WhatsApp.</li>
              <li>The secretary posts the same copy back in #Chronic Reports for documentation.</li>
            </ol>
          </div>
        </details>

        <h3>Unavailable medication and editing forms</h3>
        <ul>
          <li>The patient brings the name of an alternative available in Tafileh pharmacies. Remove the old drug and add the alternative on the form; the clinic informs the patient.</li>
          <li>Any Family Doctor can edit a patient's form on the MedNet portal (dose, quantity, adding or replacing a drug). You do not need the doctor who wrote the original prescription.</li>
          <li>Items already dispensed by the pharmacy cannot be edited.</li>
        </ul>

        <h3>Injections</h3>
        <ul>
          <li>Injections given from clinic stock must still be prescribed on the insurance form, so the patient dispenses them and returns them to the clinic.</li>
          <li>Add an "IM injection" procedure; the administration fee covers syringes.</li>
        </ul>

        <h3>Sick leaves and reports</h3>
        <ul>
          <li>You decide sick leaves and document the duration in the patient's Public Note, then tell the Tafileh secretariat, who issue and stamp the official form and send it on WhatsApp. Only your name is required; you do not need your personal stamp, as the secretariat stamps the form with the Tadawa stamp.</li>
          <li>If a GP writes a medical report for a patient you saw, the GP will ask for your approval.</li>
          <li>Eye reports and glasses prescriptions are issued by Samara Centre, not Tadawa.</li>
        </ul>
"""),

dict(id="insurance", toc="Insurance rules", kicker="Insurance", group="amber", title="Insurance rules", body=f"""
        <p class="sub-label">Accepted insurers and TPAs</p>
        <ul class="tag-list">
          <li>MedNet</li><li>Medexa</li><li>Newton</li><li>MedService – Company</li><li>MedService – Phosphate</li><li>Omni Care</li><li>Solidarity</li><li>GIG</li><li>Arab European</li><li>Bar Association</li>
        </ul>
        <p>MedService Company and MedService Phosphate are different insurers. Logins and portal steps: see the {ext(CREDS, "restricted credentials document")}.</p>

        <h3>Pricing</h3>
        <ul>
          <li>Enter every procedure price manually from the Jordanian Medical Association fee schedule. <strong>A blank price causes rejection or partial approval.</strong></li>
          <li>Price = points × point value (2.8 JOD minimum to 3.5 JOD maximum). Family Medicine and GP prices differ.</li>
          <li>Dressings (MedNet): simple 3 JOD, large 8 JOD, maximum 5 per form.</li>
          <li>If an in-clinic procedure is rejected, post the patient's name and insurance number in the {TAF} group; the responsible person contacts the insurer.</li>
        </ul>
        <div class="callout">
          <strong>Example</strong>
          <p>Family Doctor ECG: 9.6 points = 26.88–33.6 JOD.</p>
        </div>

        <h3>When a form is used</h3>
        <div class="info-grid">
          <section class="info-card"><h3>No form used</h3><p>Consultations with no medication, lab/imaging request or opened claim. Referring right after the history, with no tests.</p></section>
          <section class="info-card"><h3>Form used</h3><p>If tests are ordered, a form is used even if you refer later.</p></section>
        </div>
        <p>Referral forms never use one of the patient's forms; the receiving facility opens its own.</p>

        <h3>Follow-ups and merging</h3>
        <ul>
          <li>If the patient returns within 7 days for the same complaint, edit the original form instead of opening a new one.</li>
          <li>If several forms were opened by mistake, post in the {TAF} group: patient name, national ID, insurance ID and "<span lang="ar" dir="rtl">دمج نماذج</span>". Merging happens on working days (Sunday–Thursday). Never merge a referral form with a form that has diagnoses or labs.</li>
          <li>Before saying visits are finished, check for a visit in the last 7 days and add orders to that form. If all visits are used, the secretary asks the patient to contact their insurer; follow up once new forms are added.</li>
        </ul>

        <h3>Coverage notes</h3>
        <ul>
          <li>Corns and calluses are often treated as cosmetic; call approvals with the clinical justification.</li>
          <li>Crepe and compression bandages are usually not covered or only partly.</li>
          <li>Some plans do not cover 100%, which can lead to rejected tests.</li>
        </ul>
        <div class="callout open-point">
          <strong>If labs are rejected</strong>
          <p>Use symptoms as the diagnosis, add a justification with the "+" next to the diagnosis, or call approvals. Only Family Doctors open forms. Use the Family Doctor account for Family Medicine orders; a Family-specialist order opened on a GP-type account is rejected.</p>
        </div>
"""),

dict(id="referrals", toc="Gatekeeping and referrals", kicker="Referrals", group="amber", title="Gatekeeping and referrals", body=f"""
        <div class="callout">
          <strong>Tamweelcom</strong>
          <p>Tadawa is the exclusive, mandatory primary care provider for Tamweelcom employees (1,476 beneficiaries). All other providers are closed to them; they need a Tadawa referral.</p>
        </div>
        <ul>
          <li><strong>Emergencies:</strong> Tamweelcom patients contact Tadawa first (app or phone). You make the ER referral on MedNet.</li>
          <li><strong>Urgent referral requests from Tamweelcom HR</strong> (posted by management) are handled immediately by the Family Doctor on shift, even without a Treat Me Now call, and confirmed in the {TAF} group.</li>
        </ul>

        <details class="workflow" open>
          <summary>MedNet referral (Family Doctor)</summary>
          <div class="workflow-content">
            <ol>
              <li>Open the patient's page on MedNet with the national ID or card number and date of birth.</li>
              <li>On the left, choose "referring specialty".</li>
              <li><strong>ER referrals:</strong> select "general". Do NOT select "Emergency Medicine" or "ER" (the ER will not see it).</li>
              <li><strong>Specialty referrals:</strong> select the required specialty.</li>
              <li><strong>Diagnosis on all referrals:</strong> <em>referral of pt w/o examination or treatment</em>, even if you made a diagnosis. This stops a form being deducted.</li>
              <li>Leave "requested amount" blank and click Submit.</li>
            </ol>
            <ul>
              <li>Do not call approvals for routine referrals. Ignore hospital staff who say it should be "ER".</li>
              <li>If the hospital cannot find the referral, delete the form and create a new one with the same details; if it still fails, call MedNet approvals.</li>
              <li>If MedNet auto-fills the form or "general" is missing (usually already referred that month), do not refer on that form. Send a screenshot to MedNet approvals and ask them to approve it (through the secretary).</li>
              <li><strong>"Visited a specialty without a referral" message:</strong> check whether we referred the patient. If not, refer now; if yes, the secretary calls MedNet approvals and informs the patient.</li>
            </ul>
          </div>
        </details>

        <details class="workflow" open>
          <summary>Document the referral on Tadawa too</summary>
          <div class="workflow-content">
            <ol>
              <li>For every Treat Me Now call or appointment where you refer, open "Referrals" on Tadawa.</li>
              <li>Select the specialty. For ER referrals choose <strong>"ER / Emergency Medicine"</strong> (unlike MedNet).</li>
              <li>Set the "date From – To" fields and click Save.</li>
            </ol>
            <p>Referrals for patients who call by phone are made directly on MedNet, then documented on Tadawa: create an appointment for the patient on Tadawa, then refer the patient on the platform.</p>
          </div>
        </details>

        <h3>Referral reporting on Zoho Cliq</h3>
        <p>Whenever a patient is referred, send a message in the {TAF} group confirming that the referral has been made, with the patient's information and the referral destination.</p>
        <ul class="tag-list">
          <li>Patient name</li><li>Insurance number</li><li>Referral to (specialty / department)</li><li>Year of birth</li>
        </ul>
        <div class="info-grid">
          <section class="info-card"><h3>Emergency referral</h3><p>The secretary follows up with the patient an hour after the referral.</p></section>
          <section class="info-card"><h3>Specialist referral</h3><p>The secretary follows up the next day.</p></section>
        </div>
        <p>After the follow-up call, the secretary confirms in the same group that the patient was followed up.</p>

        <h3>Radiology in Tafileh</h3>
        <p>MedNet does not cover CT or MRI at government or military hospitals in Tafileh, and there are no other CT/MRI centres there. In emergencies the public hospital receives the patient, who signs a financial waiver. Otherwise refer to MedNet-approved imaging centres in Karak (ask in the {TAF} group for the current list).</p>
"""),

dict(id="psychiatric", toc="Psychiatric emergencies and suicide risk", kicker="Safety", group="rose", title="Psychiatric emergencies and suicide risk", body=f"""
        <p>Follow the {ext(PROTOCOL, "internal protocol")}. It applies to any patient with suicidal thoughts, intent or a recent attempt; acute psychosis endangering self or others; severe agitation or aggression; or any acute disturbance that stops them deciding safely.</p>
        <div class="callout warning">
          <strong>Immediate safety</strong>
          <p>The patient is never left alone, is moved to a safe place, and harmful objects are removed (nursing does this in clinic).</p>
        </div>
        <p><strong>Assessment:</strong> vital signs, consciousness, rule out medical causes (hypoglycaemia, hypoxia, intoxication, head injury), mental state, and suicide risk (thoughts, plan, means, intent, previous attempts, risk and protective factors).</p>
        <div class="reference-list">
          <div class="reference-row"><strong>High risk</strong><span>Plan, means, recent attempt, command hallucinations, safety cannot be ensured → call an ambulance/Civil Defence or the security authorities and transfer immediately to the ER or a hospital with psychiatry.</span></div>
          <div class="reference-row"><strong>Moderate risk</strong><span>Thoughts without a clear plan, several risk factors → consult a psychiatrist if possible; urgent referral to the ER or psychiatric clinic.</span></div>
          <div class="reference-row"><strong>Low risk</strong><span>Passing thoughts, no plan or intent, strong protective factors → safety plan, early follow-up, psychiatry referral, and involve the family with consent (or without it if needed to protect life).</span></div>
        </div>
        <p><strong>Document:</strong> times, complaint, findings, risk assessment, mental state, decision and reasons, people contacted, ambulance call time, departure time, receiving facility, and any refusal with the patient's capacity and the steps you took.</p>
"""),

dict(id="escalation", toc="Escalation", kicker="Follow-up", group="green", title="Escalation", body=f"""
        <ul>
          <li>After an emergency referral, the secretary calls the patient about an hour later and posts an update in the {TAF} group.</li>
          <li>When you need a patient followed up, ask the nurse or secretary in the {TAF} group; they call and report back.</li>
        </ul>
"""),

dict(id="reporting", toc="Reporting", kicker="Reporting", group="amber", title="Reporting", body=f"""
        <div class="callout open-point">
          <strong>One form for all reporting</strong>
          <p>All reporting goes through one form, the reporting form: {ext(REPORT_FORM, '<span lang="ar" dir="rtl">نموذج الإبلاغ عن حادث أو مشكلة</span>')}. Use the form every time, even if you already mentioned the case in a Zoho Cliq group or by phone. A message in a group is not a report.</p>
        </div>
        <p class="sub-label">Report these through the form</p>
        <ul>
          <li>Any incident, bug or error, with a screenshot or video.</li>
          <li>Problems with the Tadawa platform that patients or staff face, with the details and the action taken. Also post platform problems in #IT-Support.</li>
          <li>Wrong dosage forms in Tadawa's medication list (e.g., a tablet listed as a liquid).</li>
          <li><strong>Resistant patients:</strong> patients who refuse to comply with medical instructions or procedures.</li>
          <li><strong>Abusive patients:</strong> patients who behave abusively or inappropriately.</li>
          <li>Rare or unique medical services you provided.</li>
        </ul>
        <div class="callout">
          <strong>Why it matters</strong>
          <p>Every report lands in one place, so each case is followed up and nothing gets lost in chat messages. It gives Tadawa a documented record in line with approved procedures, which protects patients and staff. Repeated problems become visible, so they can be fixed.</p>
        </div>
        <p><a class="approval-number" href="{REPORT_FORM}" target="_blank" rel="noopener noreferrer">Open the reporting form ↗</a></p>
"""),

dict(id="phones", toc="Phone numbers", kicker="Contacts", group="teal", title="Phone numbers", body=f"""
        <h3>Tadawa</h3>
        <div class="reference-list">
          <div class="reference-row"><strong>Tadawa main (general)</strong>{tel("0793226000")}</div>
          <div class="reference-row"><strong>Tafileh clinic</strong>{tel("0793381119")}</div>
          <div class="reference-row"><strong>Amman clinic</strong>{tel("0790730275", "07 9073 0275")}</div>
          <div class="reference-row"><strong>Irbid clinic</strong>{tel("0790107082")}</div>
        </div>
        <h3>Insurer approvals</h3>
        <div class="reference-list">
          <div class="reference-row"><strong>MedNet</strong><span class="nums">{tel("065008363")}{tel("+962798580355", "+962 79 858 0355")}</span><span class="row-note">Second number: mobile</span></div>
          <div class="reference-row"><strong>Medexa</strong>{tel("065529833")}</div>
          <div class="reference-row"><strong>Solidarity</strong>{tel("065777555")}</div>
          <div class="reference-row"><strong>MedService</strong>{tel("064632965")}</div>
          <div class="reference-row"><strong>Newton</strong>{tel("065902320")}</div>
          <div class="reference-row"><strong>GIG</strong>{tel("065654665")}</div>
          <div class="reference-row"><strong>Omni Care</strong>{tel("065533757")}<span class="row-note">Ext. 103 / 105</span></div>
          <div class="reference-row"><strong>Arab European</strong><span class="nums">{tel("065518935")}{tel("0778480867")}{tel("0796666836")}</span><span class="row-note">Main 065518935 · System problems 0778480867 · 24 h approvals 0796666836 · Referrals ext. 260 / 266</span></div>
        </div>
"""),

dict(id="references", toc="Reference documents", kicker="References", group="teal", title="Reference documents", body=f"""
        <ul class="link-chips">
          <li>{ext(TM_HANDBOOK, "Tadawa Telemedicine Doctor Handbook")}</li>
          <li>{ext(CREDS, "Insurance Portals &amp; Credentials – Family Doctors Only")}</li>
          <li>{ext(PROTOCOL, "Psychiatric Emergency &amp; Suicide Risk Protocol")}</li>
          <li>{ext("https://docs.google.com/document/d/182Yje5rH_zYRrVpDJcpBUn-VYYD5IjYlcpUrruc_CH4/edit", "Tadawa platform updates")}</li>
          <li>{ext("https://drive.google.com/file/d/1kzsWn9OVC8c-79dxvlgJLvNxUqC9SGwF/view", "Tadawa Healthcare telemedicine guide (PDF)")}</li>
          <li>{ext("https://docs.google.com/document/d/1LuGgfNem2GFxA-oflqvitS7CRD9oXFYunkHs97xaIsc/edit", "Sick leave form template")}</li>
          <li>{ext("https://abdullahammartadawa.github.io/TadawaFAQs/", "Tadawa FAQs website")}</li>
        </ul>
"""),
]
