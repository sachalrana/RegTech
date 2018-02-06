namespace RegTechInterface
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.btnYes = new System.Windows.Forms.Button();
            this.btnNo = new System.Windows.Forms.Button();
            this.txtRequirements = new System.Windows.Forms.TextBox();
            this.btnChapterSelect = new System.Windows.Forms.Button();
            this.btnExit = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.BackColor = System.Drawing.Color.Transparent;
            this.label1.Cursor = System.Windows.Forms.Cursors.No;
            this.label1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.label1.Font = new System.Drawing.Font("Norwester", 26.25F);
            this.label1.ForeColor = System.Drawing.Color.White;
            this.label1.Location = new System.Drawing.Point(397, 21);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(435, 42);
            this.label1.TabIndex = 0;
            this.label1.Text = "Requirements Vertification";
            // 
            // btnYes
            // 
            this.btnYes.BackColor = System.Drawing.Color.White;
            this.btnYes.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnYes.Font = new System.Drawing.Font("Norwester", 30F);
            this.btnYes.Location = new System.Drawing.Point(851, 83);
            this.btnYes.Name = "btnYes";
            this.btnYes.Size = new System.Drawing.Size(321, 223);
            this.btnYes.TabIndex = 1;
            this.btnYes.Text = "Yes";
            this.btnYes.UseVisualStyleBackColor = false;
            this.btnYes.Click += new System.EventHandler(this.btnYes_Click);
            // 
            // btnNo
            // 
            this.btnNo.BackColor = System.Drawing.Color.White;
            this.btnNo.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnNo.Font = new System.Drawing.Font("Norwester", 30F);
            this.btnNo.Location = new System.Drawing.Point(851, 350);
            this.btnNo.Name = "btnNo";
            this.btnNo.Size = new System.Drawing.Size(321, 223);
            this.btnNo.TabIndex = 2;
            this.btnNo.Text = "No";
            this.btnNo.UseVisualStyleBackColor = false;
            this.btnNo.Click += new System.EventHandler(this.btnNo_Click);
            // 
            // txtRequirements
            // 
            this.txtRequirements.BackColor = System.Drawing.Color.White;
            this.txtRequirements.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.txtRequirements.Font = new System.Drawing.Font("Kelvetica Nobis", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtRequirements.Location = new System.Drawing.Point(35, 83);
            this.txtRequirements.Multiline = true;
            this.txtRequirements.Name = "txtRequirements";
            this.txtRequirements.Size = new System.Drawing.Size(761, 490);
            this.txtRequirements.TabIndex = 3;
            // 
            // btnChapterSelect
            // 
            this.btnChapterSelect.BackColor = System.Drawing.Color.White;
            this.btnChapterSelect.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnChapterSelect.Font = new System.Drawing.Font("Norwester", 15F);
            this.btnChapterSelect.Location = new System.Drawing.Point(497, 605);
            this.btnChapterSelect.Name = "btnChapterSelect";
            this.btnChapterSelect.Size = new System.Drawing.Size(252, 42);
            this.btnChapterSelect.TabIndex = 4;
            this.btnChapterSelect.Text = "Back to Chapter Selection";
            this.btnChapterSelect.UseVisualStyleBackColor = false;
            this.btnChapterSelect.Click += new System.EventHandler(this.btnChapterSelect_Click);
            // 
            // btnExit
            // 
            this.btnExit.BackColor = System.Drawing.Color.DarkRed;
            this.btnExit.FlatAppearance.BorderSize = 0;
            this.btnExit.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnExit.Font = new System.Drawing.Font("Norwester", 15.25F);
            this.btnExit.ForeColor = System.Drawing.Color.White;
            this.btnExit.Location = new System.Drawing.Point(1113, 618);
            this.btnExit.Name = "btnExit";
            this.btnExit.Size = new System.Drawing.Size(115, 41);
            this.btnExit.TabIndex = 20;
            this.btnExit.Text = "Logout";
            this.btnExit.UseVisualStyleBackColor = false;
            this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.LemonChiffon;
            this.BackgroundImage = global::RegTechInterface.Properties.Resources.Corporate_Finance;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(1240, 671);
            this.Controls.Add(this.btnExit);
            this.Controls.Add(this.btnChapterSelect);
            this.Controls.Add(this.txtRequirements);
            this.Controls.Add(this.btnNo);
            this.Controls.Add(this.btnYes);
            this.Controls.Add(this.label1);
            this.Font = new System.Drawing.Font("Norwester", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnYes;
        private System.Windows.Forms.Button btnNo;
        private System.Windows.Forms.TextBox txtRequirements;
        private System.Windows.Forms.Button btnChapterSelect;
        private System.Windows.Forms.Button btnExit;
    }
}

