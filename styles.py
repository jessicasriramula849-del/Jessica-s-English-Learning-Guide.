def get_custom_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;700;800;900&family=Lora:ital,wght@0,500;0,600;1,400&display=swap');

    /* Global Typography & Background */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 4rem;
        max-width: 1140px;
    }

    /* 🌈 Radiant Brand Hero Banner */
    .brand-hero {
        background: linear-gradient(135deg, #4338ca 0%, #6366f1 25%, #a855f7 55%, #ec4899 85%, #f97316 100%);
        border-radius: 24px;
        padding: 40px 44px;
        color: white;
        margin-bottom: 26px;
        box-shadow: 0 20px 35px -8px rgba(99, 102, 241, 0.35), 0 6px 12px -2px rgba(236, 72, 153, 0.2);
        position: relative;
        overflow: hidden;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    .brand-hero::before {
        content: '';
        position: absolute;
        top: -60px;
        right: -60px;
        width: 220px;
        height: 220px;
        background: radial-gradient(circle, rgba(255,255,255,0.25) 0%, rgba(255,255,255,0) 70%);
        border-radius: 50%;
        pointer-events: none;
    }

    .brand-hero h1 {
        font-family: 'Outfit', sans-serif;
        font-weight: 900;
        font-size: 2.5rem;
        margin-bottom: 10px;
        color: #ffffff !important;
        letter-spacing: -0.03em;
        text-shadow: 0 3px 12px rgba(0, 0, 0, 0.18);
        line-height: 1.15;
    }
    .brand-hero h2 {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #fef08a !important;
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: -4px;
        margin-bottom: 12px;
        letter-spacing: -0.01em;
        text-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
    }
    .brand-hero p {
        font-size: 1.12rem;
        opacity: 0.96;
        margin-bottom: 0px;
        line-height: 1.6;
        max-width: 860px;
        color: #f8fafc;
    }
    .brand-hero .subtitle-tag {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.22);
        backdrop-filter: blur(10px);
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 14px;
        border: 1px solid rgba(255, 255, 255, 0.35);
        color: #ffffff;
    }

    /* 🎨 Author Spotlight Card (Jessica) */
    .author-spotlight {
        background: linear-gradient(135deg, #ffffff 0%, #f0fdfa 50%, #eff6ff 100%);
        border: 2px solid #99f6e4;
        border-radius: 22px;
        padding: 28px;
        margin-bottom: 26px;
        box-shadow: 0 12px 28px -6px rgba(20, 184, 166, 0.15);
        display: flex;
        gap: 28px;
        align-items: center;
        flex-wrap: wrap;
    }
    .author-img-wrapper {
        position: relative;
        flex-shrink: 0;
    }
    .author-img {
        width: 170px;
        height: 230px;
        object-fit: cover;
        border-radius: 18px;
        border: 4px solid #ffffff;
        box-shadow: 0 10px 25px -4px rgba(13, 148, 136, 0.28), 0 0 15px rgba(99, 102, 241, 0.2);
    }
    .author-badge {
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(135deg, #0d9488 0%, #0284c7 100%);
        color: white;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 0.04em;
        white-space: nowrap;
        box-shadow: 0 4px 10px rgba(13, 148, 136, 0.35);
        border: 2px solid #ffffff;
    }

    /* 🎨 Alphabet Card Soundboard */
    .alphabet-card {
        background: #ffffff;
        border: 2px solid #e2e8f0;
        border-radius: 16px;
        padding: 16px 12px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 12px;
    }
    .alphabet-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 20px rgba(2, 132, 199, 0.15);
        border-color: #38bdf8;
    }
    .alphabet-letter {
        font-family: 'Outfit', sans-serif;
        font-size: 2.2rem;
        font-weight: 900;
        color: #0284c7;
        margin: 0;
        line-height: 1.1;
    }
    .alphabet-word {
        font-size: 1rem;
        font-weight: 700;
        color: #0f172a;
        margin: 4px 0 2px 0;
    }

    /* 🎨 Colorful Level Badges */
    .badge-pill {
        display: inline-block;
        padding: 5px 14px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 700;
        margin-right: 8px;
        letter-spacing: 0.03em;
        box-shadow: 0 2px 5px rgba(0,0,0,0.04);
    }
    .badge-kids { background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); color: #92400e; border: 1px solid #fcd34d; }
    .badge-student { background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%); color: #3730a3; border: 1px solid #a5b4fc; }
    .badge-adult { background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%); color: #065f46; border: 1px solid #6ee7b7; }
    .badge-pro { background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%); color: #9d174d; border: 1px solid #f9a8d4; }
    .badge-idiom { background: linear-gradient(135deg, #ede9fe 0%, #ddd6fe 100%); color: #5b21b6; border: 1px solid #c4b5fd; }
    .badge-accent { background: linear-gradient(135deg, #ffedd5 0%, #fed7aa 100%); color: #9a3412; border: 1px solid #fdba74; }

    /* 👩‍🏫 Teacher Jessica's Note Callout */
    .jessica-callout {
        background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 100%);
        border-left: 6px solid #10b981;
        border-radius: 0 18px 18px 0;
        padding: 20px 24px;
        margin: 20px 0;
        box-shadow: 0 8px 16px -4px rgba(16, 185, 129, 0.12), 0 2px 6px rgba(0,0,0,0.03);
        border-top: 1px solid #e2e8f0;
        border-right: 1px solid #e2e8f0;
        border-bottom: 1px solid #e2e8f0;
        position: relative;
    }
    .jessica-callout-header {
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        color: #065f46;
        margin-bottom: 8px;
        font-size: 1.05rem;
    }
    .jessica-callout-body {
        font-family: 'Lora', Georgia, serif;
        font-size: 1.02rem;
        color: #1e293b;
        line-height: 1.65;
    }

    /* 🌈 Pretty Custom Cards */
    .custom-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 18px;
        box-shadow: 0 10px 20px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.03);
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        overflow: hidden;
    }
    .custom-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 25px -5px rgba(99, 102, 241, 0.12), 0 10px 10px -5px rgba(99, 102, 241, 0.04);
        border-color: #cbd5e1;
    }
    .custom-card h3 {
        font-family: 'Outfit', sans-serif;
        margin-top: 4px;
        color: #0f172a;
        font-size: 1.35rem;
        font-weight: 700;
        letter-spacing: -0.01em;
    }

    /* 🎨 Colorful Theme Cards */
    .card-sunny {
        background: linear-gradient(135deg, #ffffff 0%, #fffbeb 100%);
        border-top: 4px solid #f59e0b;
    }
    .card-ocean {
        background: linear-gradient(135deg, #ffffff 0%, #eff6ff 100%);
        border-top: 4px solid #3b82f6;
    }
    .card-emerald {
        background: linear-gradient(135deg, #ffffff 0%, #ecfdf5 100%);
        border-top: 4px solid #10b981;
    }
    .card-berry {
        background: linear-gradient(135deg, #ffffff 0%, #faf5ff 100%);
        border-top: 4px solid #a855f7;
    }
    .card-rose {
        background: linear-gradient(135deg, #ffffff 0%, #fff1f2 100%);
        border-top: 4px solid #f43f5e;
    }

    /* Comparison Box (Formal vs Casual) */
    .compare-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
        margin: 16px 0;
    }
    .compare-box-casual {
        background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
        border: 1px solid #fed7aa;
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 4px 6px -1px rgba(249, 115, 22, 0.08);
    }
    .compare-box-formal {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border: 1px solid #bbf7d0;
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 4px 6px -1px rgba(16, 185, 129, 0.08);
    }

    /* Quiz feedback boxes */
    .quiz-feedback-correct {
        background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
        border: 2px solid #34d399;
        color: #064e3b;
        border-radius: 14px;
        padding: 18px 22px;
        margin-top: 14px;
        font-size: 1.02rem;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.15);
    }
    .quiz-feedback-wrong {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        border: 2px solid #f87171;
        color: #7f1d1d;
        border-radius: 14px;
        padding: 18px 22px;
        margin-top: 14px;
        font-size: 1.02rem;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.12);
    }

    /* Chat bubbles with vibrant accents */
    .chat-bubble-jessica-container {
        display: flex;
        gap: 14px;
        align-items: flex-start;
        margin-bottom: 14px;
    }
    .chat-avatar-jessica {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #3b82f6;
        box-shadow: 0 4px 8px rgba(59, 130, 246, 0.25);
        flex-shrink: 0;
    }
    .chat-bubble-jessica {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 5px solid #3b82f6;
        border-radius: 16px;
        padding: 16px 20px;
        color: #1e3a8a;
        box-shadow: 0 4px 10px rgba(59, 130, 246, 0.08);
        flex-grow: 1;
    }
    .chat-bubble-user {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border-right: 5px solid #8b5cf6;
        border-radius: 16px;
        padding: 16px 20px;
        margin-bottom: 14px;
        text-align: right;
        color: #4c1d95;
        box-shadow: 0 4px 10px rgba(139, 92, 246, 0.08);
    }

    /* Sidebar Profile Card with Jessica's Real Picture */
    .sidebar-profile {
        background: linear-gradient(135deg, #ffffff 0%, #e0f2fe 50%, #fdf4ff 100%);
        border: 2px solid #bae6fd;
        border-radius: 20px;
        padding: 20px 16px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 22px rgba(2, 132, 199, 0.14);
    }
    .sidebar-avatar {
        width: 105px;
        height: 105px;
        border-radius: 50%;
        border: 4px solid #ffffff;
        box-shadow: 0 6px 18px rgba(2, 132, 199, 0.3), 0 0 0 3px #0284c7;
        margin: 0 auto 12px auto;
        display: block;
        object-fit: cover;
    }

    /* Interactive Flip / Word Highlight */
    .word-highlight {
        background: linear-gradient(120deg, #fef08a 0%, #fed7aa 100%);
        padding: 2px 8px;
        border-radius: 6px;
        font-weight: 700;
        color: #78350f;
    }
    </style>
    """
