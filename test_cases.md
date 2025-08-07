# Test Cases for WhatsApp Application

| Test Case ID | Description | Input | Expected Output | Test Type |
|-------------|-------------|-------|----------------|-----------|
| F001 | Verify text message sending and delivery | Send "Hello" text message to a contact | Message should be delivered with proper delivery receipts (single tick, double tick) | Functional |
| F002 | Verify read receipts functionality | Read a received message | Sender should see blue ticks indicating message was read | Functional |
| F003 | Verify photo sharing in HD quality | Share a photo with HD quality option enabled | Photo should be delivered in HD quality to recipient | Functional |
| F004 | Verify video sharing | Share a 30-second video | Video should be delivered and playable by recipient | Functional |
| F005 | Verify document sharing | Share a PDF document | Document should be delivered and viewable by recipient | Functional |
| F006 | Verify status upload | Upload a photo as status | Status should be visible to contacts for 24 hours | Functional |
| F007 | Verify status view count | View a contact's status | View count should increment for the status owner | Functional |
| F008 | Verify profile picture update | Change profile picture | New profile picture should be visible to contacts | Functional |
| F009 | Verify chat backup | Initiate chat backup to cloud | Chats should be backed up successfully | Functional |
| F010 | Verify chat restore | Restore chats from backup | All backed up chats should be restored | Functional |
| F011 | Verify media download | Download a received image | Image should be saved to device gallery | Functional |
| F012 | Verify group creation | Create a new group with 5 contacts | Group should be created with all added members | Functional |
| F013 | Verify UPI transaction | Send ₹100 via UPI to a contact | Money should be transferred and transaction history updated | Functional |
| F014 | Verify contact blocking | Block a contact | No messages or calls should be received from blocked contact | Functional |
| F015 | Verify audio call | Initiate an audio call to a contact | Call should connect with clear audio | Functional |
| F016 | Verify video call | Initiate a video call to a contact | Call should connect with clear video and audio | Functional |
| F017 | Verify notification settings | Disable notifications for a specific group | No notifications should appear for messages from that group | Functional |
| F018 | Verify message search | Search for keyword "meeting" in chats | All messages containing "meeting" should be displayed | Functional |
| F019 | Verify multi-device login | Login to WhatsApp Web while using mobile app | Both devices should synchronize messages | Functional |
| F020 | Verify privacy settings | Change "Last Seen" to "Nobody" | Contacts should not be able to see user's last seen status | Functional |
| F021 | Verify chat archiving | Archive a chat | Chat should move to archived section | Functional |
| F022 | Verify message reaction | React with 👍 to a message | Reaction should be visible to all chat participants | Functional |
| F023 | Verify message forwarding | Forward a message to another contact | Message should be delivered with forwarded label | Functional |
| F024 | Verify starred messages | Star an important message | Message should appear in starred messages section | Functional |
| F025 | Verify QR code contact sharing | Scan contact's QR code | Contact should be added to address book | Functional |
| NF001 | Verify message delivery time | Send message with slow network (2G) | Message should be delivered within 10 seconds | Non-functional |
| NF002 | Verify app performance under load | Open app with 100+ active chats | App should load within 3 seconds | Non-functional |
| NF003 | Verify end-to-end encryption | Send sensitive information in a message | Message should show encryption lock icon | Non-functional |
| NF004 | Verify battery consumption | Use app for 1 hour of messaging | Battery consumption should not exceed 10% | Non-functional |
| NF005 | Verify app compatibility | Install app on different