      // Function to show content based on link clicked
      function showContent(contentType) {
        // Select the slide navigation and content elements
        var slideNav = document.getElementById('slideNav');
        var slideContent = document.getElementById('slideContent');

        // Show the slide navigation
        slideNav.style.display = 'flex';

        // Dynamically load content based on link clicked
        switch (contentType) {
            case 'about':
                document.getElementById('slideTitle').innerText = 'About Store Price List';
                document.getElementById('slideText').innerHTML = `
                <p>Welcome to Store Price List, your go-to destination for comprehensive store information and product pricing.</p>
                <p>Our web application offers a user-friendly interface where you can explore a vast array of products along</p>
                <p>with their corresponding price categories. With the added convenience of a virtual shopping cart, you can</p>
                <p>effortlessly calculate your total expenditure while customizing quantities to suit your needs. By creating</p>
                <p>an account and logging in, you unlock the ability to share valuable insights about your store and product</p>
                <p>pricing, fostering a community-driven platform where users can exchange valuable information to enhance</p>
                <p>their shopping experience. Join us today and streamline your shopping journey with Store Price List.</p>
                <br>
                <p>With Store Price List, you can:</p>
                <ul>
                    <li>Share your store information in public</li>
                    <li>Quickly update product prices</li>
                    <li>Organize products into categories</li>
                    <li>View historical price data</li>
                    <li>Generate price reports</li>
                </ul>
                <br>
                <p>Our mission is to simplify the process of managing prices for store owners and managers,allowing them to </p>
                <p>focus on providing excellent service to their customers.</p>
                <p>For any inquiries or support, feel free to <span class="highlight">contact us</span>.</p>
                `;
                break;
            
            case 'contact':
                document.getElementById('slideTitle').innerText = 'Contact';
                document.getElementById('slideText').innerHTML = `
                <p>Thank you for considering Store Price List. Should you have any inquiries, feedback, or require assistance,</p>
                <p>our dedicated team is here to support you.</p>
                <br>
                <p>Please feel free to reach out to us via the following channels:</p>
                <ul>
                    <li>Email: johnrichardorian@storepricelist.com</li>
                    <li>Phone: +1 (555) 123-4567</li>
                    <li>Address: 123 Main Street, City, State, Zip Code</li>
                </ul>
                <br>
                <p>We value your feedback and strive to provide prompt and effective assistance to ensure your experience   </p>
                <p>with Store Price List exceeds your expectations.</p>
                <p>Thank you for choosing Store Price List.</p>
                `;
                break;
            case 'terms':
                document.getElementById('slideTitle').innerText = 'Terms of Service';
                document.getElementById('slideText').innerHTML = `
                <p>Welcome to Store Price List. These terms govern your use of our services. By accessing or using Store Price</p>
                <p>List, you agree to comply with and be bound by these terms. Please read them carefully.</p>
                <p>1. Use of Services:</p>
                <p>By using Store Price List, you agree to use the services provided for lawful purposes only. You must not use</p>
                <p>our services in any way that violates any applicable laws or regulations.</p>
                <p>2. User Accounts:</p>
                <p>Creating a user account with Store Price List requires you to provide accurate and complete information. You<p>
                <p>are responsible for maintaining the security of your account and ensuring that your password remains</p>
                <p>confidential.</p>
                <p>3. Intellectual Property:</p>
                <p>All content included on Store Price List, such as text, graphics, logos, and images, is the property of Store</p>
                <p>Price List and is protected by copyright laws. You may not reproduce, distribute, modify, or create</p>
                <p>derivative works of such content without our prior written consent.</p>
                <p>4. Limitation of Liability:</p>
                <p>Store Price List and its affiliates, directors, officers, employees, agents, and suppliers shall not be liable<p>
                <p>for any indirect, incidental, special, consequential, or punitive damages arising out of or relating to your</p>
                <p>use of our services.</p>
                <p>5. Governing Law:</p>
                <p>These terms shall be governed by and construed in accordance with the laws of [Your Jurisdiction], without</p>
                <p>regard to its conflict of law provisions.</p>
                <p>By continuing to use Store Price List, you agree to abide by these terms. If you do not agree to these terms,</p>
                <p>please refrain from using our services.</p>
                <p>If you have any questions or concerns regarding these terms, please contact us at support@storepricelist.com.</p>
                `;
                break;
            case 'privacy':
                document.getElementById('slideTitle').innerText = 'Privacy Policy';
                document.getElementById('slideText').innerHTML = `
                <p>Welcome to Store Price List. This Privacy Policy outlines how we collect, use, and protect your personal</p>
                <p>information when you use our services. By accessing or using Store Price List, you consent to the terms</p>
                <p>outlined in this Privacy Policy.</p>
                <p>1. Information We Collect:</p>
                <p>We collect personal information that you provide to us when you create an account, such as your name,</p>
                <p>email address, and contact information. Additionally, we may collect usage data and analytics information</p>
                <p>when you interact with our services.</p>
                <p>2. Use of Information:</p>
                <p>We use the information collected to provide and improve our services, personalize your experience,</p>
                <p>communicate with you, and ensure the security of our platform. We may also use aggregated and anonymized</p>
                <p>data for analytical purposes.</p>
                <p>3. Data Security:</p>
                <p>We implement industry-standard security measures to protect your personal information from unauthorized</p>
                <p>access, disclosure, alteration, or destruction. However, please be aware that no method of transmission</p>
                <p>over the internet or electronic storage is 100% secure.</p>
                <p>4. Data Sharing:</p>
                <p>We do not sell, trade, or rent your personal information to third parties. However, we may share your</p>
                <p>information with trusted service providers who assist us in operating our platform, conducting our</p>
                <p>business, or servicing you.</p>
                <p>5. Your Choices:</p>
                <p>You have the right to access, update, or delete your personal information. You may also opt-out of</p>
                <p>receiving promotional communications from us at any time. Please note that certain features of our</p>
                <p>services may be unavailable if you choose to opt-out of certain communications.</p>
                `;
                break;
            default:
                document.getElementById('slideTitle').innerText = 'No Content Available';
                document.getElementById('slideText').innerText = 'No Content';
        }
    }

    // Function to close the slide navigation
    function closeSlideNav() {
        document.getElementById('slideNav').style.display = 'none';
    }
