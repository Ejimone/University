## Algorithm for WassupHq

The WassupHq algorithm is modular, with each module tailored to a specific feature—academic assistance, campus marketplace, and freelancing—while incorporating location-based services and cross-module recommendations. It aligns with the strategic refinements identified in your report, such as ethical AI use, robust quality control, and secure API integrations.

### 1. User Registration and Authentication

- **Purpose**: Ensure only college students access the platform and secure their data.
- **Input**: User's `.edu` email, personal details (e.g., name, university, location).
- **Process**:
  1. Verify the `.edu` email to confirm student status.
  2. Create a user profile with basic information.
  3. Implement secure authentication using OAuth 2.0 for API integrations (e.g., Google Classroom).
  4. Encrypt user data for privacy compliance (e.g., GDPR, CCPA).
- **Output**: Verified user account with access to app features.

---

### 2. Academic Assistance Module

This module supports students with assignments from platforms like Coursera and Google Classroom using AI and human freelancers, while upholding academic integrity.

#### 2.1. Assignment Retrieval

- **Purpose**: Fetch assignments for processing within the app.
- **Input**: User's connected accounts (e.g., Coursera, Google Classroom).
- **Process**:
  1. Use APIs (e.g., Google Classroom's `courses.courseWork.list`) to retrieve assignments.
  2. Store assignments securely in the user's account and app database.
  3. Log retrieval in an app-generated activity log (with user’s name) for admin oversight.
- **Output**: List of assignments available for assistance.

#### 2.2. AI Assistance Algorithm

- **Purpose**: Provide ethical academic support without generating full content.
- **Input**: Assignment prompt or draft, assistance type (e.g., idea generation, outlining, grammar check).
- **Process**:
  1. Analyze input using Natural Language Processing (NLP) to identify key topics and requirements.
  2. Based on assistance type:
     - **Idea Generation**: Generate a list of diverse ideas or angles.
     - **Outlining**: Create a structured outline (e.g., introduction, main points, conclusion).
     - **Grammar/Style Check**: Suggest corrections for errors and clarity.
     - **Research Support**: Provide keywords or source suggestions (with a disclaimer for student verification).
  3. Enforce ethical constraints: Prevent full content generation; limit to supportive elements.
  4. Present suggestions with explanations to enhance learning.
- **Output**: Suggestions, outlines, or corrections for student use.

#### 2.3. Freelancer Matching Algorithm

- **Purpose**: Connect students with suitable freelancers for personalized help.
- **Input**: Assignment details (subject, deadline, complexity), freelancer profiles (expertise, ratings, availability).
- **Process**:
  1. Extract assignment requirements (e.g., subject expertise needed).
  2. Filter freelancers with matching skills and availability.
  3. Rank freelancers by ratings, past performance, and proximity (if applicable).
  4. Present top matches with profiles and reviews.
- **Output**: List of recommended freelancers for student selection.

#### 2.4. Academic Integrity Algorithm

- **Purpose**: Prevent misuse of AI or freelance services.
- **Input**: Student’s draft or final submission.
- **Process**:
  1. Scan with AI content detection and plagiarism tools (e.g., QuillBot, Plagium).
  2. If flagged, alert the student with ethical use guidance.
  3. Require revisions or flag for admin review if misconduct is suspected.
- **Output**: Integrity report with warnings or suggestions.

#### 2.5. Submission Handling

- **Purpose**: Manage assignment completion and submission.
- **Input**: Completed assignment from AI/freelancer, platform requirements (e.g., Google Classroom).
- **Process**:
  1. Save completed work in the user’s account and app database.
  2. Display a success message/alert.
  3. For Google Classroom: Due to API limits (`studentSubmissions.turnIn` restricted to app-created coursework), prompt manual submission by the student.
  4. Log actions in the app’s activity log.
- **Output**: Saved assignment with manual submission instructions.

---

### 3. Campus Marketplace Module

This module enables peer-to-peer buying and selling of items (e.g., food, commodities) with a focus on location-based convenience.

#### 3.1. Listing Items

- **Purpose**: Allow students to sell items locally.
- **Input**: Item details (description, price, location), seller profile.
- **Process**:
  1. Create a listing with images and location tags.
  2. Verify listing for appropriateness (e.g., no prohibited items).
- **Output**: Published listing visible to nearby students.

#### 3.2. Marketplace Search Algorithm

- **Purpose**: Help students find items with location prioritization.
- **Input**: Search query, buyer’s location.
- **Process**:
  1. Parse query for keywords or categories.
  2. Retrieve matching listings from the database.
  3. Prioritize listings by proximity (e.g., same hostel, campus).
  4. Sort by relevance, price, or user preferences.
- **Output**: Sorted list of nearby items.

#### 3.3. Transaction Handling

- **Purpose**: Facilitate secure buying and selling.
- **Input**: Buyer’s selection, payment details.
- **Process**:
  1. Process payment via a secure gateway (e.g., Stripe) with escrow options.
  2. Coordinate delivery or pickup based on location.
  3. Confirm transaction completion and release funds.
- **Output**: Completed transaction with confirmation.

#### 3.4. Marketplace Trust Algorithm

- **Purpose**: Prevent scams and ensure trust.
- **Input**: Listing details, seller profile.
- **Process**:
  1. Analyze for suspicious patterns (e.g., low prices, vague descriptions).
  2. Review seller’s history and ratings.
  3. Flag or suspend risky listings/sellers; require verification if needed.
  4. Allow reporting of issues by users.
- **Output**: Trust score for listings and sellers.

---

### 4. Freelancing Platform Module

This module enables students to offer services and bid on jobs, focusing on university-specific and location-based opportunities.

#### 4.1. Service Listing

- **Purpose**: Allow freelancers to advertise their skills.
- **Input**: Service details (description, rates, expertise).
- **Process**:
  1. Create a profile with skills, portfolio, and university affiliation.
  2. Verify credentials (e.g., academic background) where possible.
- **Output**: Published service listing.

#### 4.2. Job Posting

- **Purpose**: Enable users to request services.
- **Input**: Job details (description, budget, location requirements).
- **Process**:
  1. Post job with clear instructions and category (e.g., tutoring, errands).
  2. Make visible to relevant freelancers.
- **Output**: Published job posting.

#### 4.3. Freelancing Job Matching Algorithm

- **Purpose**: Match freelancers to jobs efficiently.
- **Input**: Job posting, freelancer bids, profiles.
- **Process**:
  1. Evaluate bids based on price, ratings, and expertise.
  2. For location-specific jobs, prioritize nearby freelancers.
  3. Select best match or provide a shortlist to the job poster.
- **Output**: Selected freelancer or shortlist.

#### 4.4. Quality Control Algorithm

- **Purpose**: Ensure high-quality freelance deliverables.
- **Input**: Completed work from freelancer.
- **Process**:
  1. Check for plagiarism and AI content using detection tools.
  2. Collect student feedback on quality and timeliness.
  3. Update freelancer’s rating based on performance.
- **Output**: Quality assessment and updated freelancer profile.

---

### 5. Cross-Module Recommendation Algorithm

- **Purpose**: Enhance user experience with personalized suggestions.
- **Input**: Student’s current assignment or academic focus.
- **Process**:
  1. Analyze assignment to identify subject area (e.g., computer science).
  2. Search freelancing module for relevant expertise.
  3. Search marketplace for related items (e.g., textbooks).
  4. Rank recommendations by relevance, ratings, and proximity.
- **Output**: List of suggested freelancers and marketplace items.

---

### 6. Security and Privacy

- **Purpose**: Protect user data and comply with regulations.
- **Process**:
  1. Use OAuth 2.0 for secure API access (e.g., Google Classroom scopes like `classroom.coursework.me.readonly`).
  2. Encrypt sensitive data (e.g., assignments, payment info).
  3. Adhere to privacy laws (e.g., GDPR, India’s DPDPA).
  4. Avoid storing user credentials; use token-based authentication.
- **Output**: Secure, compliant data handling.

---

### 7. Admin Dashboard

- **Purpose**: Monitor and manage app operations.
- **Process**:
  1. Track user activities via app logs (e.g., assignment retrieval, transactions).
  2. Manage user accounts and resolve disputes.
  3. Analyze performance metrics for improvements.
- **Output**: Admin controls and insights.

---

### 8. Feedback and Improvement

- **Purpose**: Refine the app based on user input.
- **Process**:
  1. Collect feedback via in-app surveys or ratings.
  2. Update features and fix bugs iteratively.
- **Output**: Enhanced functionality and user satisfaction

# Frameworks and Technologies

- **Frontend**: React Native for cross-platform mobile development.
- **Backend**: FAST API with Python for RESTful APIs and Django for handling the ecomerce module.
- **Database**: PostgreSQL for structured data storage.
- **Authentication**: OAuth 2.0 for secure user authentication and API access.
- **AI Tools**: OpenAI for NLP tasks, plagiarism detection tools (e.g., QuillBot, Plagium) for academic integrity checks, Google-Gemini
- **Payment Processing**: Gpay for secure transactions in the marketplace and freelancing modules.
- **Hosting**: AWS or Heroku for scalable cloud hosting.
- **Analytics**: Google Analytics for user behavior tracking and performance metrics.
- **Image Processing**: Google Vision for image processing and recognition tasks, such as verifying item listings in the marketplace.
