from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arjun Mehta | Senior DevOps Engineer</title>
    <style>
        :root {
            --bg: #0b1220;
            --panel: #111a2e;
            --text: #dbeafe;
            --muted: #93a4c3;
            --accent: #38bdf8;
            --line: #1e2a44;
            --chip: #17233b;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Tahoma, Verdana, sans-serif;
            background: radial-gradient(circle at top right, #12203c 0%, var(--bg) 45%);
            color: var(--text);
            line-height: 1.6;
            padding: 24px;
        }

        .resume {
            max-width: 980px;
            margin: 0 auto;
            background: rgba(17, 26, 46, 0.94);
            border: 1px solid var(--line);
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 18px 40px rgba(0, 0, 0, 0.28);
        }

        .header {
            padding: 34px;
            border-bottom: 1px solid var(--line);
            background: linear-gradient(120deg, #162744 0%, #0f1a2f 100%);
        }

        .name {
            font-size: 2rem;
            color: #f8fbff;
            margin-bottom: 6px;
        }

        .role {
            font-size: 1.05rem;
            color: var(--accent);
            margin-bottom: 16px;
            letter-spacing: 0.02em;
        }

        .contact {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            color: var(--muted);
            font-size: 0.92rem;
        }

        .contact span {
            background: rgba(11, 18, 32, 0.5);
            border: 1px solid var(--line);
            border-radius: 999px;
            padding: 6px 12px;
        }

        .content {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 28px;
            padding: 30px;
        }

        h2 {
            color: #f0f9ff;
            font-size: 1.05rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 14px;
        }

        section {
            margin-bottom: 28px;
        }

        .summary {
            color: var(--muted);
            font-size: 0.97rem;
        }

        .exp-item {
            padding: 14px;
            border: 1px solid var(--line);
            border-radius: 12px;
            background: rgba(11, 18, 32, 0.42);
            margin-bottom: 12px;
        }

        .exp-title {
            display: flex;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 8px;
        }

        .exp-title strong {
            color: #f8fbff;
        }

        .exp-title span {
            color: var(--muted);
            font-size: 0.88rem;
        }

        ul {
            padding-left: 18px;
            color: var(--muted);
            font-size: 0.92rem;
        }

        .chip-wrap {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .chip {
            background: var(--chip);
            border: 1px solid var(--line);
            color: #b9cbec;
            padding: 6px 10px;
            border-radius: 8px;
            font-size: 0.84rem;
        }

        .side-card {
            border: 1px solid var(--line);
            background: rgba(11, 18, 32, 0.45);
            border-radius: 12px;
            padding: 14px;
            margin-bottom: 12px;
        }

        .side-card p,
        .side-card li {
            color: var(--muted);
            font-size: 0.9rem;
        }

        .side-card strong {
            color: #f8fbff;
        }

        @media (max-width: 860px) {
            .content {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 560px) {
            body {
                padding: 12px;
            }

            .header,
            .content {
                padding: 18px;
            }

            .name {
                font-size: 1.6rem;
            }
        }
    </style>
</head>
<body>
    <main class="resume">
        <header class="header">
            <h1 class="name">Arjun Mehta</h1>
            <p class="role">Senior DevOps Engineer</p>
            <div class="contact">
                <span>Bengaluru, India</span>
                <span>arjun.mehta.devops@email.com</span>
                <span>+91-98765-43210</span>
                <span>linkedin.com/in/arjunmehta-devops</span>
                <span>github.com/arjunmehta-devops</span>
            </div>
        </header>

        <div class="content">
            <div>
                <section>
                    <h2>Professional Summary</h2>
                    <p class="summary">
                        DevOps Engineer with 8+ years of experience building secure and scalable cloud platforms on AWS.
                        Proven track record in Kubernetes operations, CI/CD automation, and infrastructure as code.
                        Focused on reducing deployment risk, improving release frequency, and optimizing cloud cost.
                    </p>
                </section>

                <section>
                    <h2>Experience</h2>

                    <article class="exp-item">
                        <div class="exp-title">
                            <strong>Senior DevOps Engineer - CloudNest Technologies</strong>
                            <span>Mar 2022 - Present</span>
                        </div>
                        <ul>
                            <li>Designed multi-account AWS landing zone using Terraform, cutting environment provisioning time from 2 days to 40 minutes.</li>
                            <li>Built GitHub Actions pipelines for microservices with quality gates and blue-green deployments, reducing production rollback incidents by 38%.</li>
                            <li>Managed 15+ EKS clusters with centralized observability (Prometheus, Grafana, Loki).</li>
                        </ul>
                    </article>

                    <article class="exp-item">
                        <div class="exp-title">
                            <strong>DevOps Engineer - ByteBridge Systems</strong>
                            <span>Jul 2019 - Feb 2022</span>
                        </div>
                        <ul>
                            <li>Migrated legacy VM workloads to Docker and Kubernetes, improving average release cycle from bi-weekly to daily.</li>
                            <li>Implemented automated security scans (Snyk, Trivy, SonarQube) in CI pipelines.</li>
                            <li>Introduced infrastructure monitoring and alerting that reduced MTTR by 45%.</li>
                        </ul>
                    </article>
                </section>

                <section>
                    <h2>Key Projects</h2>
                    <article class="exp-item">
                        <div class="exp-title">
                            <strong>Enterprise CI/CD Platform</strong>
                            <span>2024</span>
                        </div>
                        <ul>
                            <li>Created reusable CI/CD templates for 60+ repositories across backend and frontend teams.</li>
                            <li>Added policy-as-code checks and required approvals for production promotions.</li>
                        </ul>
                    </article>
                    <article class="exp-item">
                        <div class="exp-title">
                            <strong>Disaster Recovery Automation</strong>
                            <span>2023</span>
                        </div>
                        <ul>
                            <li>Automated cross-region RDS and S3 recovery workflows with Lambda and Step Functions.</li>
                            <li>Reduced DR drill execution time from 6 hours to 90 minutes.</li>
                        </ul>
                    </article>
                </section>
            </div>

            <aside>
                <section>
                    <h2>Technical Skills</h2>
                    <div class="chip-wrap">
                        <span class="chip">AWS</span>
                        <span class="chip">Terraform</span>
                        <span class="chip">Kubernetes</span>
                        <span class="chip">Docker</span>
                        <span class="chip">GitHub Actions</span>
                        <span class="chip">Jenkins</span>
                        <span class="chip">Argo CD</span>
                        <span class="chip">Prometheus</span>
                        <span class="chip">Grafana</span>
                        <span class="chip">Linux</span>
                        <span class="chip">Bash</span>
                        <span class="chip">Python</span>
                    </div>
                </section>

                <section>
                    <h2>Certifications</h2>
                    <div class="side-card">
                        <ul>
                            <li>AWS Certified DevOps Engineer - Professional</li>
                            <li>Certified Kubernetes Administrator (CKA)</li>
                            <li>HashiCorp Terraform Associate</li>
                        </ul>
                    </div>
                </section>

                <section>
                    <h2>Education</h2>
                    <div class="side-card">
                        <p><strong>B.Tech, Computer Science</strong><br>Visvesvaraya Technological University</p>
                    </div>
                </section>

                <section>
                    <h2>Highlights</h2>
                    <div class="side-card">
                        <ul>
                            <li>8+ years in DevOps and platform engineering</li>
                            <li>99.95% service uptime target ownership</li>
                            <li>Mentored 20+ engineers in cloud-native practices</li>
                        </ul>
                    </div>
                </section>
            </aside>
        </div>
    </main>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(TEMPLATE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
