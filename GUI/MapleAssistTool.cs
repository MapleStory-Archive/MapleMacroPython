using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.Serialization;
using System.IO;
using Newtonsoft.Json;

namespace MapleAssistToolPy
{


	public partial class MapleAssistTool : Form
	{
		public MapleAssistTool()
		{
			InitializeComponent();
		}

		MapleGuiUtil util = new MapleGuiUtil();

		private void Form1_Load(object sender, EventArgs e)
		{

		}

		private void panel1_Paint(object sender, PaintEventArgs e)
		{

		}

		private void LuminousButton_Click(object sender, EventArgs e)
		{

		}

		private void panel1_Paint_1(object sender, PaintEventArgs e)
		{

		}

		private void CaveLoadAisleUp_Click(object sender, EventArgs e)
		{
			util.execStartUp(this.UWSC_RadioButton.Checked,CaveLoadAisleUp.Text);
		}
	}
}
