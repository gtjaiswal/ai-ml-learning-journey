# WEEK 14 LEARNING GUIDE: GDPR + Secrets Management + Security Hardening

**Timeline:** February 16-22, 2026  
**Total Time:** ~11-12 hours  
**Focus:** Production security hardening, GDPR compliance, secrets management

---

## 📋 WEEK OVERVIEW

**What You'll Build:**
- AWS Secrets Manager integration (zero hardcoded credentials)
- Complete GDPR compliance system
- Security hardening across entire application
- Automated security scanning pipeline

**What You'll Learn:**
- Secrets management best practices
- GDPR compliance requirements
- Encryption at rest and in transit
- Security scanning and vulnerability detection
- Audit logging for compliance

**Time Allocation:**
- Mon-Fri: 1-1.5 hours/day (7-7.5h total)
- Weekend: 4-4.5 hours (2-2.5h Sat, 2h Sun)
- Total: 11-12 hours

---

## DAY 1 (MONDAY): Secrets Management Fundamentals

**Time:** 1.5 hours

---

### SESSION 1: Understanding Secrets Management (45 min)

**Theory (25 min):**

**Video 1: "What is Secrets Management?"** - HashiCorp  
- URL: https://www.youtube.com/watch?v=5W_Q01_E7hQ
- Duration: 9:48
- What you'll learn: Why secrets management matters, common vulnerabilities

**Video 2: "AWS Secrets Manager Overview"**  
- URL: https://www.youtube.com/watch?v=Y5n3kYnHDU0
- Duration: 10:06
- What you'll learn: AWS Secrets Manager features, rotation capabilities

**Reading:**
📖 **AWS Secrets Manager Documentation**  
- URL: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
- Duration: 10 min read
- Focus: "What is Secrets Manager?" and "Common scenarios"

**What you need to understand:**
1. Why hardcoded credentials are dangerous?
2. What happens when API keys leak to GitHub?
3. How does automatic rotation work?
4. What's the difference between Secrets Manager and Parameter Store?
5. When to use each service?

**Reflection Questions:**
Write answers to:
- What secrets exist in your current RAG system?
- Where are they currently stored?
- What would happen if your .env file was committed to GitHub?
- How would you handle key rotation without downtime?

---

### SESSION 2: Secrets Audit & Migration Plan (45 min)

**Hands-On Exercise: Secrets Inventory**

**Requirements:**
Create `SECRETS_AUDIT.md` documenting:

**1. Current Secrets Inventory:**
List every secret in your system:
- OpenAI API key
- Database password
- JWT secret key
- OAuth client secrets
- AWS access keys
- Any other API keys

For each secret, document:
- Current storage location (.env file? hardcoded?)
- Who has access?
- When was it last rotated?
- What would break if it changed?

**2. Risk Assessment:**
For each secret, rate risk:
- **CRITICAL**: Database password, AWS keys (system down if compromised)
- **HIGH**: OpenAI API key (costly abuse, data exposure)
- **MEDIUM**: JWT secret (user sessions compromised)
- **LOW**: Non-sensitive config values

**3. Migration Priority:**
Order secrets by:
1. Risk level (Critical first)
2. Ease of migration (Simple first)
3. Dependencies (Least dependent first)

**What to figure out:**
- How many secrets do you actually have?
- Which secrets are shared across environments?
- Which secrets need rotation capability?
- What's the minimal set needed for the system to run?

**Success criteria:**
✅ Complete inventory of all secrets  
✅ Risk rating for each  
✅ Clear migration order  
✅ Identified secrets that need auto-rotation  
✅ Documented what breaks if each secret changes

---

## DAY 2 (TUESDAY): AWS Secrets Manager Integration

**Time:** 1.5 hours

---

### SESSION 1: AWS Secrets Manager Setup (45 min)

**Video:** "AWS Secrets Manager Tutorial"  
- URL: https://www.youtube.com/watch?v=jLj8wA8fBYo
- Duration: 20:56
- Watch: First 20 minutes (creation, retrieval, basic usage)

**Reading:**
📖 **Getting Started with Secrets Manager**  
- URL: https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html
- Duration: 15 min read

**Hands-On Exercise: Create Secrets in AWS**

**Requirements:**

**1. Install AWS CLI:**
Verify you have AWS CLI configured with credentials.

**2. Create Secrets Manually:**
Use AWS Console to create these secrets:
- `fraud-detection/openai-api-key`
- `fraud-detection/database-url`
- `fraud-detection/jwt-secret`

For each secret:
- Choose appropriate description
- Enable automatic rotation (where applicable)
- Tag with: Environment=dev, Application=fraud-detection
- Set resource policy (who can access)

**3. Test Retrieval:**
Use AWS CLI to retrieve secrets:
```bash
aws secretsmanager get-secret-value --secret-id fraud-detection/openai-api-key
```

Verify you can:
- List all secrets
- Get secret value
- Update secret value
- Describe secret metadata

**What to figure out:**
- How to structure secret names (hierarchical naming)
- How to version secrets
- How tags help organize secrets
- Cost implications (pricing per secret per month)
- IAM permissions needed for retrieval

**Success criteria:**
✅ Secrets created in AWS Secrets Manager  
✅ Can retrieve via AWS CLI  
✅ Proper naming convention established  
✅ Tags applied correctly  
✅ Understand pricing model

---

### SESSION 2: Python Integration (45 min)

**Reading:**
📖 **Boto3 Secrets Manager Documentation**  
- URL: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html
- Duration: 15 min read

**Hands-On Exercise: Secrets Client**

**Requirements:**
Create `secrets_client.py` module:

**1. Secrets Retrieval Function:**
Build function that:
- Accepts secret name as parameter
- Retrieves from AWS Secrets Manager
- Caches secrets in memory (avoid repeated calls)
- Handles errors gracefully
- Returns parsed secret value

**2. Connection String Builder:**
Build function that:
- Retrieves database credentials from Secrets Manager
- Constructs PostgreSQL connection string
- Handles individual components (host, port, user, password, database)
- Returns formatted connection string

**3. Configuration Loader:**
Build function that:
- Loads all application secrets at startup
- Validates required secrets exist
- Populates configuration object
- Handles missing secrets gracefully

**4. Error Handling:**
Handle these scenarios:
- Secret doesn't exist
- AWS credentials not configured
- Network timeout
- Invalid secret format
- Insufficient IAM permissions

**What to figure out:**
- How to cache secrets (how long? when to refresh?)
- How to handle secret updates without restart
- Error messages for missing secrets
- Whether to fail fast or use defaults
- How to structure configuration object

**Success criteria:**
✅ Can retrieve secrets from Python  
✅ Secrets cached to avoid repeated API calls  
✅ Database connection string built from secrets  
✅ All error cases handled  
✅ No secrets logged or printed

---

## DAY 3 (WEDNESDAY): GDPR Compliance Foundation

**Time:** 1.5 hours

---

### SESSION 1: Understanding GDPR (45 min)

**Video 1: "GDPR Explained"**  
- URL: https://www.youtube.com/watch?v=Assdm6fIHlE
- Duration: 6:06
- What you'll learn: Core GDPR principles

**Video 2: "GDPR for Developers"**  
- URL: https://www.youtube.com/watch?v=5UZzZJVT6rY
- Duration: 28:44
- Watch: First 20 minutes (technical requirements)

**Reading:**
📖 **GDPR Developer Guide**  
- URL: https://gdpr.eu/
- Duration: 20 min read
- Focus: "Right to be forgotten", "Right to data portability"

**What you need to understand:**
1. What is personal data under GDPR?
2. What are the key rights (access, rectification, erasure, portability)?
3. What constitutes consent?
4. How long can you retain data?
5. What are the penalties for non-compliance?

**Key GDPR Principles:**

**Lawfulness, Fairness, Transparency:**
- Must have legal basis for processing
- Users must know what you're doing with data
- Clear privacy policies

**Purpose Limitation:**
- Only collect data for specific purposes
- Can't repurpose data without new consent

**Data Minimization:**
- Only collect what you actually need
- Don't store unnecessary personal data

**Accuracy:**
- Keep personal data accurate and up-to-date
- Allow users to correct their data

**Storage Limitation:**
- Don't keep data longer than necessary
- Define retention periods

**Integrity & Confidentiality:**
- Protect data with appropriate security
- Prevent unauthorized access

**Accountability:**
- Document compliance measures
- Be able to demonstrate compliance

---

### SESSION 2: GDPR Requirements Mapping (45 min)

**Hands-On Exercise: GDPR Compliance Matrix**

**Requirements:**
Create `GDPR_COMPLIANCE.md` documenting:

**1. Data Inventory:**
For your fraud detection system, list:

**Personal Data Collected:**
- User accounts (email, name, role)
- Query logs (user ID, timestamp, query text)
- Audit logs (user actions, IP addresses)
- Search history
- Document access logs

For each, document:
- Why collected (purpose)
- Legal basis (consent, legitimate interest, contract)
- Retention period
- Who has access
- Where stored (database, logs, backups)

**2. GDPR Rights Implementation Plan:**

**Right to Access (Article 15):**
- User requests all their personal data
- What data do you return?
- What format (JSON, CSV, PDF)?
- How do you authenticate the request?
- Deadline: 30 days

**Right to Rectification (Article 16):**
- User requests correction of data
- What data can be corrected?
- How do you verify corrections?

**Right to Erasure (Article 17):**
- User requests deletion
- What gets deleted?
- What must be retained (legal obligations)?
- How to handle backups?
- Deadline: 30 days

**Right to Data Portability (Article 20):**
- User requests data in machine-readable format
- What data included?
- What format (JSON standard)?

**3. Consent Management:**
- When do you ask for consent?
- How is consent recorded?
- Can users withdraw consent?
- What happens when consent withdrawn?

**4. Breach Notification:**
- How do you detect data breaches?
- Who gets notified?
- Timeline: 72 hours to authorities, "without undue delay" to users
- What information included in notification?

**What to figure out:**
- What personal data do you actually store?
- Which GDPR rights apply to your system?
- What's technically feasible vs legally required?
- How to handle edge cases (e.g., user in training data)?
- Retention periods for different data types

**Success criteria:**
✅ Complete personal data inventory  
✅ Legal basis documented for each data type  
✅ Retention periods defined  
✅ Implementation plan for each GDPR right  
✅ Consent workflow designed  
✅ Breach response plan outlined

---

## DAY 4 (THURSDAY): Encryption & Audit Logging

**Time:** 1.5 hours

---

### SESSION 1: Encryption Fundamentals (45 min)

**Video:** "Encryption Explained"  
- URL: https://www.youtube.com/watch?v=AQDCe585Lnc
- Duration: 6:07
- Core concepts of encryption

**Video:** "TLS/SSL Explained"  
- URL: https://www.youtube.com/watch?v=j9QmMEWmcfo
- Duration: 5:24
- How HTTPS works

**Reading:**
📖 **AWS Encryption Documentation**  
- URL: https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/encryption.html
- Duration: 20 min read

**What you need to understand:**

**Encryption at Rest:**
- Database encryption (PostgreSQL)
- S3 bucket encryption (PDFs)
- EBS volume encryption
- Encryption keys management (AWS KMS)

**Encryption in Transit:**
- TLS/SSL for API endpoints
- Database connections (SSL mode)
- Internal service communication
- Certificate management

**Key Management:**
- AWS KMS (Key Management Service)
- Customer managed keys vs AWS managed
- Key rotation policies
- Access control to keys

---

### SESSION 2: Audit Logging Design (45 min)

**Video:** "Audit Logging Best Practices"  
- URL: https://www.youtube.com/watch?v=pCy1c3vH6fY
- Duration: 18:03
- Watch: First 15 minutes

**Reading:**
📖 **AWS CloudWatch Logs**  
- URL: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html
- Duration: 10 min read

**Hands-On Exercise: Audit Log Design**

**Requirements:**
Create `AUDIT_LOGGING_SPEC.md`:

**1. Events to Log:**

**User Authentication:**
- Login attempts (success/failure)
- Logout events
- Password changes
- Failed authentication reasons
- IP address, user agent

**Data Access:**
- Search queries executed
- Documents accessed
- Filters applied
- Results returned
- User who performed action

**Data Modifications:**
- User created/updated/deleted
- Permissions changed
- Configuration changes
- Who made change, what changed, when

**API Usage:**
- All API endpoints called
- Request parameters
- Response status codes
- Response times
- Rate limiting events

**Security Events:**
- Failed authorization attempts
- Suspicious activity patterns
- API key usage
- Token generation/revocation

**2. Log Structure:**
Design JSON format for each event type:
```json
{
  "timestamp": "ISO 8601",
  "event_type": "search_query",
  "user_id": "UUID",
  "ip_address": "redacted or hashed",
  "action": "description",
  "resource": "what was accessed",
  "result": "success/failure",
  "metadata": {...}
}
```

**3. PII in Logs:**
Decide for each field:
- Should it be logged?
- Should it be redacted?
- Should it be hashed?
- How long to retain?

**4. Log Retention:**
Define retention periods:
- Authentication logs: ?
- Search queries: ?
- Audit events: ?
- Error logs: ?
- Compliance considerations (GDPR, SOX, etc.)

**5. Log Access Control:**
- Who can view logs?
- How to prevent log tampering?
- Centralized logging strategy
- Log encryption

**What to figure out:**
- What's too much vs too little logging?
- How to log without storing PII?
- How to make logs searchable?
- How to alert on suspicious patterns?
- Cost implications of logging everything

**Success criteria:**
✅ Complete list of events to audit  
✅ Structured log format defined  
✅ PII handling policy for logs  
✅ Retention periods defined  
✅ Access control plan  
✅ Integration points identified (CloudWatch, Elasticsearch)

---

## DAY 5 (FRIDAY): Input Validation & Security Headers

**Time:** 1 hour

---

### SESSION 1: Input Validation (30 min)

**Video:** "Input Validation Security"  
- URL: https://www.youtube.com/watch?v=nH4r6xv-qGg
- Duration: 7:52
- Common validation mistakes

**Reading:**
📖 **OWASP Input Validation Cheat Sheet**  
- URL: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
- Duration: 15 min read

**Hands-On Exercise: Validation Rules**

**Requirements:**
Create `INPUT_VALIDATION_RULES.md`:

**1. API Input Validation:**

For each endpoint, define validation:

**Search Query:**
- Max length: ? characters
- Allowed characters: alphanumeric, spaces, punctuation
- Blocked patterns: SQL injection, script tags
- Sanitization: HTML escape, SQL escape

**User Registration:**
- Email: valid email format, max length
- Password: min 12 chars, complexity requirements
- Name: max length, allowed characters
- Role: must be from allowed enum

**Document Upload:**
- File type: allowed extensions (PDF only)
- File size: max size (10MB?)
- Filename: sanitize special characters
- Content type validation

**2. SQL Injection Prevention:**
How to prevent:
- Parameterized queries only
- ORM validation
- Input sanitization
- What characters to block/escape

**3. XSS Prevention:**
How to prevent:
- HTML escaping all outputs
- Content-Security-Policy headers
- Input sanitization
- Safe templating

**4. Path Traversal Prevention:**
For file operations:
- Validate file paths
- Prevent ../ sequences
- Whitelist directories
- Canonicalize paths

**What to figure out:**
- How strict to be vs usability
- Where to validate (client vs server vs both)
- How to give helpful error messages
- When to sanitize vs reject

**Success criteria:**
✅ Validation rules for all inputs  
✅ SQL injection prevention documented  
✅ XSS prevention strategy  
✅ Path traversal protection  
✅ Clear reject vs sanitize decisions

---

### SESSION 2: Security Headers (30 min)

**Reading:**
📖 **OWASP Secure Headers**  
- URL: https://owasp.org/www-project-secure-headers/
- Duration: 15 min read

**Reading:**
📖 **Security Headers Guide**  
- URL: https://securityheaders.com/
- Duration: 10 min (test your current site)

**Hands-On Exercise: Headers Configuration**

**Requirements:**
Create `SECURITY_HEADERS.md` documenting:

**1. Required Headers:**

For each header, document:
- What it does
- Why it's needed
- Value to use

**Headers to configure:**
```
Strict-Transport-Security
Content-Security-Policy
X-Content-Type-Options
X-Frame-Options
X-XSS-Protection
Permissions-Policy
Referrer-Policy
```

**2. CORS Configuration:**
Define CORS policy:
- Allowed origins (which domains can call API)
- Allowed methods (GET, POST, etc.)
- Allowed headers
- Credentials allowed?
- Preflight cache duration

**3. Rate Limiting:**
Define rate limits:
- Per user limits (100 requests/hour?)
- Per IP limits (500 requests/hour?)
- Per endpoint limits (search: 10/min, auth: 5/min)
- What happens when exceeded (429 status, retry-after header)

**What to figure out:**
- Which headers are critical vs nice-to-have
- CSP policy that doesn't break your app
- CORS settings that are secure but functional
- Reasonable rate limits

**Success criteria:**
✅ All security headers configured  
✅ CORS policy defined  
✅ Rate limiting strategy  
✅ Tested headers don't break app  
✅ Headers validated on securityheaders.com

---

## DAY 6 (SATURDAY): Automated Security Scanning

**Time:** 2.5 hours

---

### SESSION 1: SAST with Bandit (60 min)

**Video:** "Static Application Security Testing (SAST)"  
- URL: https://www.youtube.com/watch?v=OQGDO4W1h2M
- Duration: 6:49
- What SAST tools do

**Reading:**
📖 **Bandit Documentation**  
- URL: https://bandit.readthedocs.io/en/latest/
- Duration: 15 min read

**Hands-On Exercise: Bandit Setup**

**Requirements:**

**1. Install and Run Bandit:**
Install Bandit on your codebase.

Run against your Python code:
```bash
bandit -r . -f json -o bandit-report.json
```

**2. Analyze Results:**
Review Bandit findings:
- High severity issues
- Medium severity issues
- Low severity issues

For each finding:
- What's the vulnerability?
- Is it a real issue or false positive?
- How to fix it?
- Can it be ignored (with justification)?

**3. Create Baseline:**
Document acceptable baseline:
- Which warnings are acceptable?
- Which must be fixed?
- Create .bandit configuration file
- Exclude false positives

**4. CI/CD Integration:**
Plan how to integrate into CI/CD:
- Run on every commit?
- Fail build on high severity?
- Generate reports
- Track trends over time

**What to figure out:**
- How to interpret Bandit output
- How to distinguish real issues from false positives
- How strict to be (zero warnings vs acceptable baseline)
- How to handle third-party library warnings

**Success criteria:**
✅ Bandit installed and running  
✅ Full security scan completed  
✅ All high-severity issues analyzed  
✅ Baseline configuration created  
✅ CI/CD integration planned

---

### SESSION 2: Dependency Scanning (45 min)

**Reading:**
📖 **Safety Documentation**  
- URL: https://github.com/pyupio/safety
- Duration: 10 min read

**Reading:**
📖 **Dependabot Overview**  
- URL: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates
- Duration: 15 min read

**Hands-On Exercise: Dependency Scanning**

**Requirements:**

**1. Safety Check:**
Run Safety against your dependencies:
```bash
safety check --file requirements.txt
```

Analyze:
- Known vulnerabilities in dependencies
- Severity levels
- Affected versions
- Fixed versions available
- CVE details

**2. Create Dependency Policy:**
Document policy:
- How often to scan (daily, weekly, per commit)?
- Who reviews vulnerability reports?
- How quickly to patch (critical: 24h, high: 7 days, etc.)?
- When to accept risk vs upgrade?

**3. Enable Dependabot:**
Configure Dependabot for your repository:
- Enable security updates
- Enable version updates
- Configure update schedule
- Set auto-merge rules (minor versions only)

**4. Vulnerable Dependency Matrix:**
Create `DEPENDENCIES_VULNERABILITIES.md`:

For each vulnerable dependency:
- Package name and current version
- Vulnerability description (CVE)
- Severity (Critical/High/Medium/Low)
- Fixed version
- Upgrade path (direct or breaking change?)
- Timeline to fix

**What to figure out:**
- How to prioritize vulnerability fixes
- When to upgrade vs find alternative package
- How to test after dependency updates
- Balance security vs stability

**Success criteria:**
✅ Safety scan completed  
✅ All vulnerabilities documented  
✅ Dependabot enabled  
✅ Patch timeline defined  
✅ Critical vulnerabilities addressed immediately

---

### SESSION 3: Container Scanning with Trivy (45 min)

**Video:** "Container Security Scanning"  
- URL: https://www.youtube.com/watch?v=YQLdg_lKVzk
- Duration: 8:22
- Why scan containers

**Reading:**
📖 **Trivy Documentation**  
- URL: https://trivy.dev/latest/docs/
- Duration: 15 min read

**Hands-On Exercise: Trivy Container Scanning**

**Requirements:**

**1. Install Trivy:**
Install Trivy scanner.

**2. Scan Docker Images:**
Scan your application container:
```bash
trivy image your-app:latest
```

Analyze:
- OS package vulnerabilities
- Application dependency vulnerabilities
- Misconfigurations
- Secrets in image layers

**3. Scan Infrastructure as Code:**
Scan your docker-compose.yml:
```bash
trivy config docker-compose.yml
```

Look for:
- Insecure configurations
- Missing security settings
- Exposed ports
- Weak passwords

**4. Create Remediation Plan:**
Document in `CONTAINER_SECURITY.md`:

For each finding:
- Vulnerability or misconfiguration
- Risk level
- Remediation steps
- Whether fixable or acceptable risk

**5. Integrate into CI/CD:**
Plan integration:
- Scan on every build
- Fail builds on critical vulnerabilities
- Generate reports
- Track remediation progress

**What to figure out:**
- Which base images are most secure
- How to reduce image vulnerabilities
- Multi-stage builds for smaller attack surface
- How often to rebuild images (weekly for patches?)

**Success criteria:**
✅ Trivy installed and configured  
✅ Full container scan completed  
✅ Vulnerabilities documented  
✅ Remediation plan created  
✅ CI/CD integration designed  
✅ Critical vulnerabilities fixed

---

## DAY 7 (SUNDAY): GDPR Implementation & Testing

**Time:** 2 hours

---

### SESSION 1: GDPR Endpoints Implementation (60 min)

**Hands-On Exercise: GDPR API Endpoints**

**Requirements:**
Design (don't implement) these GDPR endpoints:

**1. GET /api/v1/gdpr/my-data**
**Purpose:** Right to Access (Article 15)

**Requirements:**
- Returns all user's personal data
- Includes: profile, queries, audit logs, documents accessed
- Format: JSON with structured sections
- Excludes: derived data, anonymized data
- Authentication required (can only access own data)
- Response within 30 days (async job for large datasets)

**What to design:**
- Response structure
- What data included
- How to gather from multiple sources
- How to handle large datasets
- Authentication/authorization

**2. DELETE /api/v1/gdpr/delete-account**
**Purpose:** Right to Erasure (Article 17)

**Requirements:**
- Deletes all user personal data
- Exceptions: legal retention requirements
- Cascade deletes (queries, logs, sessions)
- Handles backups (mark for deletion)
- Confirmation required (prevent accidents)
- Audit log of deletion
- 30-day grace period before permanent deletion

**What to design:**
- Deletion workflow
- What gets deleted vs anonymized vs retained
- Backup handling
- Confirmation mechanism
- Audit trail

**3. PATCH /api/v1/gdpr/correct-data**
**Purpose:** Right to Rectification (Article 16)

**Requirements:**
- Allows user to correct their data
- Fields: name, email, preferences
- Immutable fields: user_id, creation_date
- Validation of corrections
- Audit log of changes

**What to design:**
- Which fields correctable
- Validation rules
- Change tracking
- Approval workflow (if needed)

**4. GET /api/v1/gdpr/export-data**
**Purpose:** Right to Data Portability (Article 20)

**Requirements:**
- Exports user data in machine-readable format
- Format: JSON (standard schema)
- Includes: profile, query history, preferences
- Downloadable file
- Expires after 7 days

**What to design:**
- Export format (JSON schema)
- What data included
- File generation (async job)
- Download link security
- Expiration handling

**5. POST /api/v1/gdpr/consent**
**Purpose:** Consent Management

**Requirements:**
- Record user consent for data processing
- Granular consent (analytics, marketing, etc.)
- Timestamp of consent
- Ability to withdraw consent
- Audit log of consent changes

**What to design:**
- Consent types
- Consent storage
- Withdrawal workflow
- Impact of withdrawal

**What to figure out:**
- How to implement these without breaking system
- Performance implications
- Testing strategy
- User communication
- Timeline to build

**Success criteria:**
✅ All 5 endpoints designed  
✅ Request/response formats defined  
✅ Data flow documented  
✅ Edge cases identified  
✅ Implementation complexity estimated

---

### SESSION 2: Security Testing & Validation (60 min)

**Hands-On Exercise: Security Test Plan**

**Requirements:**
Create `SECURITY_TEST_PLAN.md`:

**1. OWASP Top 10 Testing:**

For each vulnerability, define test:

**A1: Broken Access Control:**
- Test: Try accessing other user's data
- Test: Try admin endpoints as regular user
- Test: Bypass RBAC with parameter manipulation
- Expected: All attempts blocked with 403

**A2: Cryptographic Failures:**
- Test: Check database encryption
- Test: Verify HTTPS enforcement
- Test: Check secrets in code/logs
- Expected: All data encrypted, no plaintext secrets

**A3: Injection:**
- Test: SQL injection attempts in search
- Test: Command injection in file uploads
- Test: LDAP injection in auth
- Expected: All attempts blocked/escaped

**A4: Insecure Design:**
- Test: Rate limiting effectiveness
- Test: Account lockout after failed logins
- Test: Password complexity enforcement
- Expected: All security controls working

**A5: Security Misconfiguration:**
- Test: Default credentials don't work
- Test: Unnecessary services disabled
- Test: Error messages don't leak info
- Expected: Secure configuration verified

**A6: Vulnerable Components:**
- Test: Run Safety and Trivy scans
- Test: Check for outdated dependencies
- Expected: No known vulnerabilities

**A7: Authentication Failures:**
- Test: Weak password attempts
- Test: Brute force protection
- Test: Session timeout
- Expected: Strong auth enforced

**A8: Software/Data Integrity:**
- Test: Verify signed packages
- Test: Check CI/CD pipeline security
- Expected: Integrity verified

**A9: Logging Failures:**
- Test: Security events logged
- Test: Logs tamper-proof
- Test: Log retention working
- Expected: Complete audit trail

**A10: Server-Side Request Forgery:**
- Test: SSRF attempts via file upload
- Test: SSRF via URL parameters
- Expected: All attempts blocked

**2. Penetration Testing Checklist:**

Manual tests to perform:
- Try to bypass authentication
- Attempt privilege escalation
- Test for XSS in all inputs
- Test CSRF protection
- Try path traversal attacks
- Test for information disclosure
- Attempt DOS attacks
- Test API rate limiting

**3. Compliance Validation:**

GDPR compliance tests:
- Test data export functionality
- Test data deletion completeness
- Verify consent management
- Check privacy policy accessibility
- Test right to rectification

Security compliance tests:
- All secrets in Secrets Manager
- No hardcoded credentials
- Encryption enabled everywhere
- Audit logs working
- Security headers present

**4. Automated Testing:**

Plan for automated security tests:
- Integrate Bandit into CI/CD
- Run Safety check on every commit
- Schedule weekly Trivy scans
- Automated OWASP ZAP scans
- Regular penetration test scans

**What to figure out:**
- How to test without breaking production
- How to automate testing
- How to prioritize findings
- How to track remediation
- When to hire professional penetration testers

**Success criteria:**
✅ Complete OWASP Top 10 test plan  
✅ Penetration testing checklist  
✅ GDPR compliance tests defined  
✅ Automated testing planned  
✅ Know how to verify each security control

---

## 📚 ADDITIONAL RESOURCES

**Secrets Management:**
- HashiCorp Vault: https://www.vaultproject.io/docs
- AWS Systems Manager Parameter Store: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html

**GDPR:**
- GDPR Portal: https://gdpr.eu/
- ICO Guide for Developers: https://ico.org.uk/for-organisations/guide-to-data-protection/

**Security:**
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Cheat Sheets: https://cheatsheetseries.owasp.org/
- CWE Top 25: https://cwe.mitre.org/top25/

**Tools:**
- Bandit: https://bandit.readthedocs.io/
- Safety: https://pyup.io/safety/
- Trivy: https://trivy.dev/
- OWASP ZAP: https://www.zaproxy.org/

---

## ✅ WEEK 14 DELIVERABLES

**Documentation:**
- [ ] SECRETS_AUDIT.md - Complete secrets inventory
- [ ] GDPR_COMPLIANCE.md - GDPR implementation plan
- [ ] AUDIT_LOGGING_SPEC.md - Audit logging design
- [ ] INPUT_VALIDATION_RULES.md - Validation rules
- [ ] SECURITY_HEADERS.md - Headers configuration
- [ ] DEPENDENCIES_VULNERABILITIES.md - Vulnerability matrix
- [ ] CONTAINER_SECURITY.md - Container security plan
- [ ] SECURITY_TEST_PLAN.md - Complete test plan

**Implementation Plans:**
- [ ] AWS Secrets Manager migration plan
- [ ] GDPR endpoints design
- [ ] Encryption strategy
- [ ] Security scanning CI/CD integration
- [ ] Audit logging implementation

**Security Scans:**
- [ ] Bandit scan completed
- [ ] Safety scan completed
- [ ] Trivy scan completed
- [ ] All critical vulnerabilities addressed

**Understanding:**
- [ ] Can explain secrets management benefits
- [ ] Can explain GDPR rights and requirements
- [ ] Can explain encryption at rest vs in transit
- [ ] Can explain OWASP Top 10 vulnerabilities
- [ ] Can explain security scanning tools

---

## 🎯 SUCCESS CRITERIA

**By end of Week 14, you should be able to:**

**Conceptual:**
- Explain why hardcoded secrets are dangerous
- Explain GDPR rights and how to implement them
- Explain encryption at rest and in transit
- Explain OWASP Top 10 vulnerabilities
- Explain why audit logging is critical

**Practical:**
- Migrate secrets to AWS Secrets Manager
- Design GDPR-compliant endpoints
- Configure security headers
- Run security scans (Bandit, Safety, Trivy)
- Create comprehensive test plan

**Portfolio Impact:**
This week adds:
- ✅ Production-grade security (major differentiator)
- ✅ GDPR compliance (enterprise requirement)
- ✅ Automated security scanning
- ✅ Complete audit trail
- ✅ Interview-ready security knowledge

---

**Total Learning Time:** 11-12 hours  
**Implementation Time (Week 15+):** ~15-20 hours  
**Portfolio Impact:** Critical - Production security is non-negotiable

---

**Next Week:** Month 4-5 begins - AI Agents with Phase 2 cohort!

---

**Document Generated:** December 26, 2025  
**For:** Week 14 - GDPR + Secrets Management + Security Hardening  
**Part of:** Enterprise Security Module (Weeks 12-14)