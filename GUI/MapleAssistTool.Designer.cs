namespace MapleAssistToolPy
{
	partial class MapleAssistTool
	{
		/// <summary>
		/// 必要なデザイナー変数です。
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// 使用中のリソースをすべてクリーンアップします。
		/// </summary>
		/// <param name="disposing">マネージ リソースを破棄する場合は true を指定し、その他の場合は false を指定します。</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows フォーム デザイナーで生成されたコード

		/// <summary>
		/// デザイナー サポートに必要なメソッドです。このメソッドの内容を
		/// コード エディターで変更しないでください。
		/// </summary>
		private void InitializeComponent()
		{
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MapleAssistTool));
			this.MenuPanel = new System.Windows.Forms.Panel();
			this.PythonRadioButton = new System.Windows.Forms.RadioButton();
			this.UWSC_RadioButton = new System.Windows.Forms.RadioButton();
			this.execModeLabel = new System.Windows.Forms.Label();
			this.SettingButton = new System.Windows.Forms.Button();
			this.LuminousButton = new System.Windows.Forms.Button();
			this.KannnaButton = new System.Windows.Forms.Button();
			this.UtilButton = new System.Windows.Forms.Button();
			this.LuminousPanel = new System.Windows.Forms.Panel();
			this.button1 = new System.Windows.Forms.Button();
			this.ChuChu = new System.Windows.Forms.Button();
			this.honsyo3 = new System.Windows.Forms.Button();
			this.CaveLoadAisleUp = new System.Windows.Forms.Button();
			this.MenuPanel.SuspendLayout();
			this.LuminousPanel.SuspendLayout();
			this.SuspendLayout();
			// 
			// MenuPanel
			// 
			this.MenuPanel.BackColor = System.Drawing.SystemColors.ActiveCaption;
			this.MenuPanel.Controls.Add(this.PythonRadioButton);
			this.MenuPanel.Controls.Add(this.UWSC_RadioButton);
			this.MenuPanel.Controls.Add(this.execModeLabel);
			this.MenuPanel.Controls.Add(this.SettingButton);
			this.MenuPanel.Controls.Add(this.LuminousButton);
			this.MenuPanel.Controls.Add(this.KannnaButton);
			this.MenuPanel.Controls.Add(this.UtilButton);
			this.MenuPanel.Location = new System.Drawing.Point(0, -2);
			this.MenuPanel.Name = "MenuPanel";
			this.MenuPanel.Size = new System.Drawing.Size(126, 498);
			this.MenuPanel.TabIndex = 0;
			this.MenuPanel.Paint += new System.Windows.Forms.PaintEventHandler(this.panel1_Paint);
			// 
			// PythonRadioButton
			// 
			this.PythonRadioButton.AutoSize = true;
			this.PythonRadioButton.Location = new System.Drawing.Point(65, 20);
			this.PythonRadioButton.Name = "PythonRadioButton";
			this.PythonRadioButton.Size = new System.Drawing.Size(58, 16);
			this.PythonRadioButton.TabIndex = 6;
			this.PythonRadioButton.Text = "Python";
			this.PythonRadioButton.UseVisualStyleBackColor = true;
			// 
			// UWSC_RadioButton
			// 
			this.UWSC_RadioButton.AutoSize = true;
			this.UWSC_RadioButton.Checked = global::MapleAssistToolPy.Properties.Settings.Default.UWSC_Button;
			this.UWSC_RadioButton.Cursor = System.Windows.Forms.Cursors.Default;
			this.UWSC_RadioButton.DataBindings.Add(new System.Windows.Forms.Binding("Checked", global::MapleAssistToolPy.Properties.Settings.Default, "UWSC_Button", true, System.Windows.Forms.DataSourceUpdateMode.OnPropertyChanged));
			this.UWSC_RadioButton.Location = new System.Drawing.Point(4, 20);
			this.UWSC_RadioButton.Name = "UWSC_RadioButton";
			this.UWSC_RadioButton.Size = new System.Drawing.Size(55, 16);
			this.UWSC_RadioButton.TabIndex = 5;
			this.UWSC_RadioButton.TabStop = true;
			this.UWSC_RadioButton.Text = "UWSC";
			this.UWSC_RadioButton.UseVisualStyleBackColor = true;
			// 
			// execModeLabel
			// 
			this.execModeLabel.AutoSize = true;
			this.execModeLabel.Location = new System.Drawing.Point(3, 5);
			this.execModeLabel.Name = "execModeLabel";
			this.execModeLabel.Size = new System.Drawing.Size(56, 12);
			this.execModeLabel.TabIndex = 0;
			this.execModeLabel.Text = "execMode";
			// 
			// SettingButton
			// 
			this.SettingButton.Location = new System.Drawing.Point(0, 471);
			this.SettingButton.Name = "SettingButton";
			this.SettingButton.Size = new System.Drawing.Size(123, 24);
			this.SettingButton.TabIndex = 4;
			this.SettingButton.Text = "Setting";
			this.SettingButton.UseVisualStyleBackColor = true;
			// 
			// LuminousButton
			// 
			this.LuminousButton.Location = new System.Drawing.Point(3, 40);
			this.LuminousButton.Name = "LuminousButton";
			this.LuminousButton.Size = new System.Drawing.Size(123, 54);
			this.LuminousButton.TabIndex = 2;
			this.LuminousButton.Text = "Luminous";
			this.LuminousButton.UseVisualStyleBackColor = true;
			this.LuminousButton.Click += new System.EventHandler(this.LuminousButton_Click);
			// 
			// KannnaButton
			// 
			this.KannnaButton.Location = new System.Drawing.Point(3, 93);
			this.KannnaButton.Name = "KannnaButton";
			this.KannnaButton.Size = new System.Drawing.Size(123, 54);
			this.KannnaButton.TabIndex = 4;
			this.KannnaButton.Text = "Kannna";
			this.KannnaButton.UseVisualStyleBackColor = true;
			// 
			// UtilButton
			// 
			this.UtilButton.Location = new System.Drawing.Point(3, 146);
			this.UtilButton.Name = "UtilButton";
			this.UtilButton.Size = new System.Drawing.Size(123, 54);
			this.UtilButton.TabIndex = 3;
			this.UtilButton.Text = "Util";
			this.UtilButton.UseVisualStyleBackColor = true;
			// 
			// LuminousPanel
			// 
			this.LuminousPanel.BackColor = System.Drawing.Color.Transparent;
			this.LuminousPanel.Controls.Add(this.button1);
			this.LuminousPanel.Controls.Add(this.ChuChu);
			this.LuminousPanel.Controls.Add(this.honsyo3);
			this.LuminousPanel.Controls.Add(this.CaveLoadAisleUp);
			this.LuminousPanel.Location = new System.Drawing.Point(132, 3);
			this.LuminousPanel.Name = "LuminousPanel";
			this.LuminousPanel.Size = new System.Drawing.Size(503, 314);
			this.LuminousPanel.TabIndex = 1;
			// 
			// button1
			// 
			this.button1.Location = new System.Drawing.Point(8, 141);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(123, 54);
			this.button1.TabIndex = 7;
			this.button1.Text = "ユニオン";
			this.button1.UseVisualStyleBackColor = true;
			// 
			// ChuChu
			// 
			this.ChuChu.Location = new System.Drawing.Point(8, 35);
			this.ChuChu.Name = "ChuChu";
			this.ChuChu.Size = new System.Drawing.Size(123, 54);
			this.ChuChu.TabIndex = 6;
			this.ChuChu.Text = "チューチュー(奥)";
			this.ChuChu.UseVisualStyleBackColor = true;
			// 
			// honsyo3
			// 
			this.honsyo3.Location = new System.Drawing.Point(137, 35);
			this.honsyo3.Name = "honsyo3";
			this.honsyo3.Size = new System.Drawing.Size(123, 54);
			this.honsyo3.TabIndex = 5;
			this.honsyo3.Text = "本性が現れる場所3";
			this.honsyo3.UseVisualStyleBackColor = true;
			// 
			// CaveLoadAisleUp
			// 
			this.CaveLoadAisleUp.Location = new System.Drawing.Point(266, 35);
			this.CaveLoadAisleUp.Name = "CaveLoadAisleUp";
			this.CaveLoadAisleUp.Size = new System.Drawing.Size(123, 54);
			this.CaveLoadAisleUp.TabIndex = 3;
			this.CaveLoadAisleUp.Text = "ケーヴロードの通路(上)";
			this.CaveLoadAisleUp.UseVisualStyleBackColor = true;
			this.CaveLoadAisleUp.Click += new System.EventHandler(this.CaveLoadAisleUp_Click);
			// 
			// MapleAssistTool
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
			this.ClientSize = new System.Drawing.Size(751, 495);
			this.Controls.Add(this.LuminousPanel);
			this.Controls.Add(this.MenuPanel);
			this.Name = "MapleAssistTool";
			this.Text = "MapleAssistTool version : 0.3";
			this.Load += new System.EventHandler(this.Form1_Load);
			this.MenuPanel.ResumeLayout(false);
			this.MenuPanel.PerformLayout();
			this.LuminousPanel.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.Panel MenuPanel;
		private System.Windows.Forms.Button LuminousButton;
		private System.Windows.Forms.Button UtilButton;
		private System.Windows.Forms.Button KannnaButton;
		private System.Windows.Forms.Button SettingButton;
		private System.Windows.Forms.Panel LuminousPanel;
		private System.Windows.Forms.Label execModeLabel;
		private System.Windows.Forms.RadioButton radioButton2;
		private System.Windows.Forms.GroupBox excModeGroup;
		private System.Windows.Forms.RadioButton radioButton1;
		private System.Windows.Forms.RadioButton UWSC_RadioButton;
		private System.Windows.Forms.RadioButton PythonRadioButton;
		private System.Windows.Forms.Button CaveLoadAisleUp;
		private System.Windows.Forms.Button button1;
		private System.Windows.Forms.Button ChuChu;
		private System.Windows.Forms.Button honsyo3;
	}
}

