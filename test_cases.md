# Test Cases for WhatsApp Application

| Test Case ID | Description | Input | Expected Output | Test Type |
|--------------|-------------|-------|-----------------|-----------|
| F001 | Verify text message sending | Send "Hello" to a contact | Message delivered with single tick, then double tick when delivered to recipient's device, blue tick when read | Functional |
| F002 | Verify image sharing | Share an image from gallery | Image should be delivered and visible to recipient | Functional |
| F003 | Verify video sharing in HD | Share a video with HD quality option selected | Video should be delivered in HD quality | Functional |
| F004 | Verify status upload | Upload an image as status | Status should be visible to contacts for 24 hours | Functional |
| F005 | Verify status privacy settings | Set status privacy to "My Contacts except..." and select contacts | Status should be visible to all contacts except those selected | Functional |
| F006 | Verify profile picture update | Upload a new profile picture | New profile picture should be visible to contacts based on privacy settings | Functional |
| F007 | Verify chat backup | Initiate manual backup | Chat history should be backed up to cloud storage | Functional |
| F008 | Verify chat restore | Reinstall app and restore from backup | All previous chats should be restored | Functional |
| F009 | Verify media download | Receive an image and download it | Image should be saved to device gallery | Functional |
| F010 | Verify group creation | Create a new group and add 5 contacts | Group should be created with all added contacts as members | Functional |
| F011 | Verify UPI transaction | Send ₹100 to a contact via UPI | Money should be transferred and transaction receipt shown | Functional |
| F012 | Verify contact blocking | Block a contact | Should not receive messages or calls from blocked contact | Functional |
| F013 | Verify audio call | Initiate audio call to a contact | Call should connect with clear audio | Functional |
| F014 | Verify video call | Initiate video call to a contact | Call should connect with clear video and audio | Functional |
| F015 | Verify notification settings | Disable notifications for a specific group | No notifications should appear for messages in that group | Functional |
| F016 | Verify message search | Search for a specific text in chat history | All messages containing the search text should be displayed | Functional |
| F017 | Verify multi-device login | Login to WhatsApp Web while using mobile app | Both devices should show synchronized messages | Functional |
| F018 | Verify last seen privacy | Set last seen to "Nobody" | Contacts should not see user's last seen timestamp | Functional |
| F019 | Verify chat archiving | Archive a chat | Chat should move to archived section | Functional |
| F020 | Verify message reactions | React with thumbs up emoji to a message | Emoji reaction should appear on the message | Functional |
| F021 | Verify message forwarding | Forward a message to another contact | Message should be delivered with "Forwarded" label | Functional |
| F022 | Verify starred messages | Star an important message | Message should appear in starred messages section | Functional |
| F023 | Verify QR code contact sharing | Generate and scan QR code | Contact should be added to recipient's contacts | Functional |
| F024 | Verify document sharing | Share a PDF document | Document should be delivered and viewable by recipient | Functional |
| F025 | Verify voice message | Record and send voice message | Voice message should be playable by recipient | Functional |
| NF001 | Verify message delivery time | Send message with slow network connection | Message should be delivered within 5 seconds | Non-functional |
| NF002 | Verify app performance under load | Open app with 1000+ messages in history | App should load within 3 seconds | Non-functional |
| NF003 | Verify end-to-end encryption | Send a message and check encryption status | Lock icon should appear indicating encrypted message | Non-functional |
| NF004 | Verify UI consistency across platforms | Compare UI elements on Android and iOS | UI elements should be consistent with platform guidelines | Non-functional |
| NF005 | Verify app reliability