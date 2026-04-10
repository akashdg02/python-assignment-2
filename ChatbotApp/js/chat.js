$(document).ready(function() {
    // === Variables & State ===
    const $chatInput = $('#chat-input');
    const $sendBtn = $('#send-btn');
    const $chatMessages = $('#chat-messages');
    const $welcomeSection = $('#welcome-section');
    const $sidebar = $('#sidebar');
    const $sidebarOverlay = $('#sidebar-overlay');
    const $mobileMenuBtn = $('#mobile-menu-btn');
    const $newChatBtn = $('#new-chat-btn');
    // === Bonus: Dark Mode Toggle ===
    $('#theme-toggle').on('click', function() {
        const $body = $('body');
        const $icon = $(this).find('i');
        
        if ($body.attr('data-theme') === 'dark') {
            $body.removeAttr('data-theme');
            $icon.removeClass('fa-sun').addClass('fa-moon');
            $(this).removeClass('btn-outline-light bg-dark').addClass('btn-outline-secondary bg-white');
        } else {
            $body.attr('data-theme', 'dark');
            $icon.removeClass('fa-moon').addClass('fa-sun');
            $(this).removeClass('btn-outline-secondary bg-white').addClass('btn-outline-light bg-dark');
        }
    });
    // === Part 4.2: Mobile Menu Interactions ===

    // Open sidebar when hamburger menu is clicked
    $mobileMenuBtn.on('click', function() {
        $sidebar.addClass('show');
        $sidebarOverlay.removeClass('d-none').addClass('show');
    });

    // Close sidebar when clicking the dark overlay
    $sidebarOverlay.on('click', function() {
        $sidebar.removeClass('show');
        $sidebarOverlay.removeClass('show').addClass('d-none');
    });

    // Handle "New Chat" button click
    $newChatBtn.on('click', function() {
        // Clear all messages and hide the chat area
        $chatMessages.empty().addClass('d-none');
        // Bring back the welcome screen
        $welcomeSection.removeClass('d-none');
        // Reset the state
        isFirstMessage = true;
        
        // If on mobile, close the sidebar after clicking "New Chat"
        if ($(window).width() <= 768) {
            $sidebar.removeClass('show');
            $sidebarOverlay.removeClass('show').addClass('d-none');
        }
    });
    
    // We use this to know when to hide the welcome screen
    let isFirstMessage = true;

    // Part 3.3: Mock AI Responses array
    const aiResponses = [
        "That's a great question! Based on my knowledge, I'd say you're on the right track.",
        "I can certainly help with that. Could you provide a bit more detail so I can give you the best answer?",
        "Here is a simple explanation to get you started: The key is to break the problem down into smaller steps.",
        "Interesting perspective. I hadn't thought of it quite like that before.",
        "Let me process that for a moment... Yes, that makes perfect sense. Here is how we can proceed."
    ];

    // === Part 3.2: Input Handling ===

    // Auto-resize textarea and manage send button state as user types
    $chatInput.on('input', function() {
        // Reset height to auto to calculate the new scrollHeight
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';

        // Enable button if there is text, disable if empty
        if ($(this).val().trim().length > 0) {
            $sendBtn.removeAttr('disabled');
        } else {
            $sendBtn.attr('disabled', 'disabled');
        }
    });

    // Handle Enter key for sending, Shift+Enter for new line
    $chatInput.on('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault(); // Stop it from making a new line
            if ($(this).val().trim().length > 0) {
                handleUserMessage();
            }
        }
    });

    // Handle Send Button click
    $sendBtn.on('click', function() {
        handleUserMessage();
    });

    // Make suggestion cards clickable
    $('.suggestion-card').on('click', function() {
        // Grab the text from the card title and description
        const title = $(this).find('.card-title').text();
        const desc = $(this).find('.card-text').text();
        
        $chatInput.val(title + " " + desc);
        $sendBtn.removeAttr('disabled');
        handleUserMessage(); // Automatically send it
    });

    // === Part 3.1 & 3.3: Message Processing ===

    function handleUserMessage() {
        const text = $chatInput.val().trim();
        if (!text) return; // Prevent empty messages

        // Hide welcome screen and show chat container on the very first message
        if (isFirstMessage) {
            $welcomeSection.addClass('d-none');
            $chatMessages.removeClass('d-none');
            isFirstMessage = false;
        }

        // 1. Show the user's message
        addMessage(text, 'user');

        // 2. Clear input and reset its height
        $chatInput.val('');
        $chatInput.css('height', 'auto');
        $sendBtn.attr('disabled', 'disabled');

        // 3. Show the typing animation
        showTypingIndicator();

        // 4. Simulate a network delay (1.5 seconds) before AI replies
        setTimeout(function() {
            // Remove the typing indicator
            $('#typing-indicator').remove();
            
            // Pick a random mock response
            const randomIndex = Math.floor(Math.random() * aiResponses.length);
            const reply = aiResponses[randomIndex];
            
            addMessage(reply, 'ai');
        }, 1500); 
    }

    // Function to generate the HTML for a message bubble
    function addMessage(text, sender) {
        // Get current time formatted as HH:MM AM/PM
        const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        let messageHtml = '';

        if (sender === 'user') {
            // Replace newlines with <br> tags so multi-line text formats correctly
            const formattedText = text.replace(/\n/g, '<br>');
            
            messageHtml = `
                <div class="d-flex justify-content-end mb-4">
                    <div class="p-3 rounded-4 shadow-sm" style="background-color: var(--user-msg-bg); max-width: 80%;">
                        <div class="d-flex justify-content-between align-items-center mb-1">
                            <span class="fw-bold" style="font-size: 0.9rem;">You</span>
                            <span class="text-muted small ms-3">${time}</span>
                        </div>
                        <p class="m-0">${formattedText}</p>
                    </div>
                    <div class="ms-2 mt-1">
                        <div class="rounded-circle bg-secondary text-white d-flex align-items-center justify-content-center" style="width: 35px; height: 35px;">
                            <i class="fas fa-user small"></i>
                        </div>
                    </div>
                </div>
            `;
        } else {
            messageHtml = `
                <div class="d-flex justify-content-start mb-4">
                    <div class="me-2 mt-1">
                        <div class="rounded-circle text-white d-flex align-items-center justify-content-center" style="background-color: var(--accent-color); width: 35px; height: 35px;">
                            <i class="fas fa-robot small"></i>
                        </div>
                    </div>
                    <div class="p-3 rounded-4 shadow-sm" style="background-color: var(--ai-msg-bg); max-width: 80%;">
                        <div class="d-flex justify-content-between align-items-center mb-1">
                            <span class="fw-bold" style="color: var(--accent-color); font-size: 0.9rem;">Assistant</span>
                            <span class="text-muted small ms-3">${time}</span>
                        </div>
                        <p class="m-0">${text}</p>
                    </div>
                </div>
            `;
        }

        $chatMessages.append(messageHtml);
        scrollToBottom();
    }

    // Helper function to show the animated bouncing dots
    function showTypingIndicator() {
         const typingHtml = `
            <div class="d-flex justify-content-start mb-4" id="typing-indicator">
                <div class="me-2 mt-1">
                     <div class="rounded-circle text-white d-flex align-items-center justify-content-center" style="background-color: var(--accent-color); width: 35px; height: 35px;">
                        <i class="fas fa-robot small"></i>
                    </div>
                </div>
                <div class="p-3 rounded-4 shadow-sm d-flex align-items-center" style="background-color: var(--ai-msg-bg);">
                    <div class="spinner-grow spinner-grow-sm text-secondary me-1" role="status" style="width: 0.4rem; height: 0.4rem;"></div>
                    <div class="spinner-grow spinner-grow-sm text-secondary me-1" role="status" style="width: 0.4rem; height: 0.4rem; animation-delay: 0.2s;"></div>
                    <div class="spinner-grow spinner-grow-sm text-secondary" role="status" style="width: 0.4rem; height: 0.4rem; animation-delay: 0.4s;"></div>
                </div>
            </div>`;
        $chatMessages.append(typingHtml);
        scrollToBottom();
    }

    // Always keep the newest messages in view
    function scrollToBottom() {
        $chatMessages.scrollTop($chatMessages[0].scrollHeight);
    }
});